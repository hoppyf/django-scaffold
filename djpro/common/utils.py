from decimal import Decimal


def format_decimal(decimal: Decimal):
    """
    decimal转str，用于接口返回输出，保留两位小数
    :param decimal:
    :return:
    """
    return str(round(decimal + Decimal(0.001), 2))


def format_datetime(datetime):
    """
    datetime格式化yyyy-MM-dd HH:mm:ss
    :param datetime:
    :return:
    """
    return datetime.strftime('%Y-%m-%d %H:%M:%S')


def format_date(date):
    """
    date格式化yyyy-MM-dd
    :param date:
    :return:
    """
    return date.strftime('%Y-%m-%d')
