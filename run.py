import requests


def check_date(name, id, date):
    url = 'https://hyyy.mzj.shenyang.gov.cn/api/appointments/calendar?org_id=%s&start_date=%s&end_date=%s&business_type=1'
    target = url % (str(id), date, date)
    resp = requests.get(target)
    data = resp.json()
    hours = data.get(date).get('hours')
    flag = False
    for item in hours:
        if item.get('enabled') == True and item.get('remain_count') > 0:
            print('%s - %s有名额%s个' %
                  (name, item.get('start_time'), str(item.get('remain_count'))))
            flag = True
    if not flag:
        print('%s - 无名额' % name)


def batch_check(target_date):
    print('##### %s #####' % target_date)
    check_date('铁西', 13, target_date)
    check_date('和平', 5, target_date)
    check_date('皇姑', 11, target_date)
    check_date('沈河', 7, target_date)
    check_date('大东', 9, target_date)
    check_date('沈北', 21, target_date)


if __name__ == '__main__':
    # batch_check('2023-05-15')
    # batch_check('2023-05-22')
    batch_check('2023-05-27')
    # batch_check('2023-05-28')
