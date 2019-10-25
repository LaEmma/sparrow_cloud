# -*- coding: utf-8 -*-


"""
requests 的封装， 返回的原生数据

"""

import requests
from sparrow_cloud.registry.service_discovery import consul_service


def get(service_conf, api_path, timeout=5, *args, **kwargs):
    """
    service_conf: 服务配置
    :param service_conf:
    :param api_path:
    :param args:
    :param kwargs:
    :return:
    """
    url = _build_url(service_conf, api_path)
    res = requests.get(url, timeout=timeout, *args, **kwargs)
    return res


def post(service_conf, api_path, timeout=5, *args, **kwargs):
    """
    service_conf: settings 里面配置的服务注册 key 值
    :param service_conf:
    :param api_path:
    :param args:
    :param kwargs:
    :return:
    """
    url = _build_url(service_conf, api_path)
    res = requests.post(url, timeout=timeout, *args, **kwargs)
    return res


def put(service_conf, api_path, timeout=5, *args, **kwargs):
    """
    :param service_conf: settings 里面配置的服务注册 key 值
    :param api_path:
    :param timeout:
    :param args:
    :param kwargs:
    :return:
    """
    url = _build_url(service_conf, api_path)
    res = requests.put(url, timeout=timeout, *args, **kwargs)
    return res


def delete(service_conf, api_path, timeout=5, *args, **kwargs):
    """

    :param service_conf: settings 里面配置的服务注册 key 值
    :param api_path:
    :param timeout:
    :param args:
    :param kwargs:
    :return:
    """
    url = _build_url(service_conf, api_path)
    res = requests.delete(url, timeout=timeout, *args, **kwargs)
    return res


def _build_url(service_conf, api_path):
    """
    :param service_conf:
    :param api_path:
    :return:
    """
    servicer_addr = consul_service(service_conf)
    return "http://{}{}".format(servicer_addr, api_path)

