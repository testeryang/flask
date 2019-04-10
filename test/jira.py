from flask import Blueprint, json
from jira import JIRA

jiratest = Blueprint('jiratest', __name__)

jira = JIRA("http://bug.corp.36kr.com",basic_auth=('17010054196','Ab123456'))    # a username/password tuple
def jiramath(version):
    # 找到报告人为admin的所有问题
    issues = jira.search_issues('project = JZAPP AND issuetype = Bug AND affectedVersion = '+version,maxResults=1000)
    return str(issues.__len__())
def cantdomath(version):
    issues2 = jira.search_issues('project = JZAPP AND issuetype = Bug AND affectedVersion = '+version+' AND status in (Open, "In Progress", Reopened)',maxResults=1000)
    cantdomath = str(issues2.__len__())
    return cantdomath
def openmath(version):
    issues = jira.search_issues('project = JZAPP AND issuetype = Bug AND affectedVersion = '+version+' AND status = Open',maxResults=1000)
    openmath = str(issues.__len__())
    return openmath
def closemath(version):
    issues = jira.search_issues('project = JZAPP AND issuetype = Bug AND affectedVersion = '+version+' AND status = Closed',maxResults=1000)
    closemath = str(issues.__len__())
    return closemath
@jiratest.route('/getallbug')
def jiravalue():
    list=[]
    list.append(openmath('5.3.2'))
    list.append(cantdomath('5.3.2'))
    list.append(closemath('5.3.2'))
    listvalue = json.dumps(list)
    return listvalue