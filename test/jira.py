from flask import Blueprint, json, render_template
from jira import JIRA
import requests

jiratest = Blueprint('jiratest', __name__)
jira = JIRA("http://bug.corp.36kr.com", basic_auth=('17010054196', 'Ab123456'))  # a username/password tuple

version='5.3.2'

def jiramath(version):
    # 找到报告人为admin的所有问题
    issues = jira.search_issues('project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version, maxResults=1000)
    return str(issues.__len__())


def cantdomath():
    issues2 = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND status in (Open, "In Progress", Reopened)',
        maxResults=1000)
    cantdomath = str(issues2.__len__())
    return cantdomath


def OKmath():
    issues = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND status = Resolved',
        maxResults=1000)
    OKmath = str(issues.__len__())
    return OKmath


def closemath():
    issues = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND status = Closed',
        maxResults=1000)
    closemath = str(issues.__len__())
    return closemath


@jiratest.route('/getallbug')
def jiravalue():
    list1 = {"name": "未解决BUG", "value": cantdomath()}
    list2 = {"name": "已解决BUG", "value": OKmath()}
    list3 = {"name": "关闭的BUG", "value": closemath()}
    listarr = [list1, list2, list3]
    jsonlist = json.dumps(listarr)
    return jsonlist


@jiratest.route('/getjirausername')
def getjirausername():
    issues1 = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND assignee in ("huangyuxi")',
        maxResults=1000)
    closemath1 = str(issues1.__len__())
    issues2 = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND assignee in ("董建琴")',
        maxResults=1000)
    closemath2 = str(issues2.__len__())
    issues3 = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND assignee in ("方琪中")',
        maxResults=1000)
    closemath3 = str(issues3.__len__())
    issues4 = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND assignee in ("18238671446")',
        # 贾剑峰
        maxResults=1000)
    closemath4 = str(issues4.__len__())
    issues5 = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version +' AND assignee in ("李博翰")',
        maxResults=1000)
    closemath5 = str(issues5.__len__())
    issues6 = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND assignee in ("申龙")',
        maxResults=1000)
    closemath6 = str(issues6.__len__())
    issues7 = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND assignee in ("吴迪")',
        maxResults=1000)
    closemath7 = str(issues7.__len__())
    issues8 = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND assignee in ("武河")',
        maxResults=1000)
    closemath8 = str(issues8.__len__())
    issues9 = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND assignee in ("杨杰")',
        maxResults=1000)
    closemath9 = str(issues9.__len__())
    issues10 = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND assignee in ("杨洋")',
        maxResults=1000)
    closemath10 = str(issues10.__len__())
    issues11 = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND assignee in ("zhangliansheng")',
        maxResults=1000)
    closemath11 = str(issues11.__len__())
    issues12 = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND assignee in ("朱思美")',
        maxResults=1000)
    closemath12 = str(issues12.__len__())
    issues13 = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND assignee in ("闫大卫")',
        maxResults=1000)
    closemath13 = str(issues13.__len__())
    issues14 = jira.search_issues(
        'project = JZAPP AND issuetype = Bug AND affectedVersion = ' + version + ' AND assignee is EMPTY',
        maxResults=1000)
    closemath14 = str(issues14.__len__())
    list = [closemath1, closemath2, closemath3, closemath4, closemath5, closemath6, closemath7, closemath8, closemath9,
            closemath10, closemath11, closemath12, closemath13, closemath14]
    jsonlist = json.dumps(list)
    return jsonlist

@jiratest.route('/getpersonbug')
def getpersonbug():
    return render_template('/main/personbugmath.html')

@jiratest.route("/getlog")
def aclog():
    value2=jira.dashboard(11300)
    # print(jira.dashboards())
    # print(value2.item(11602))
    # print(requests.get("http://bug.corp.36kr.com/rest/api/2/dashboard/11300/gadget/11602").text)
    # print(jira._get_items_from_page(item_type=,items_key=,resource=))
    print(jira.issue('JZAPP-2886').raw)
    print(jira.issue('JZAPP-2886').fields.summary)
    return '1'
