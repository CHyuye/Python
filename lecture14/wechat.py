# coding:utf-8

from flask import Flask, request, abort
import hashlib

# 常量 -- 微信的token令牌
WECHAT_TOKEN = "hanyuye"


app = Flask(__name__)


@app.route("/wechat/hye")
def wecaht():
    """对接微信服务公众号服务器"""
    # 接收微信服务器发送的参数
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")

    # 校验参数
    if not all([signature, timestamp, nonce, echostr]):
        abort(404)

    # 按照微信的流程进行计算签名
    li = [WECHAT_TOKEN, timestamp, nonce]
    # 排序
    li.sort()
    # 拼接字符串
    tmp_str = "".join(li)
    # 进行sha1加密, 得到正确签名值
    sign = hashlib.sha1(tmp_str).hexdigest()
    # 将自己的计算签名与 请求签名参数对比，如果相同则证明来自微信
    if signature != sign:
        #  表示请求不是微信
        abort(403)
    else:
        return echostr


if __name__ == '__main__':
    app.run(port=8000, debug=True)