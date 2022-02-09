<p align="center">
    <a href="https://github.com/MarkusJoe/FlaskRequestCounter">
        <img src="https://img.shields.io/badge/Python-3.9.x-blue.svg" alt="PythonVersion">
        <img src="https://img.shields.io/badge/LINCESE-Apache2.0-orange.svg" alt="LICENSE">
        <img src="https://img.shields.io/badge/Falsk-2.0.2-purple" alt="FlaskVersion">
    </a>
</p>

<img style="text-align: center" src="http://36.134.138.141:5000/get?name=MarkusJoe&theme=lewd" alt="Counter">

## Python 版访问次数计数器使用了flask 作为服务端接收请求
*  [文档](https://request-counter-docs.vercel.app/#/)
### 开源
- 本项目以[Apache-2.0](./LICENSE)许可开源, 即:
  - 你可以直接使用该项目提供的功能, 无需任何授权
  - 你可以在**注明来源版权信息**的情况下对源代码进行任意分发和修改以及衍生
  
## 部署
> 由于对`vercel`不熟悉, vercel的配置文件搞不明白所以暂时没有vercel的配置文件, 我也试了很多方法去部署但是要么是500要么是400

> 在部署之前你需要先安装`python3.10.x`以上的版本 
### 部署到本地服务器
 ```shell
 $ git clone https://github.com/MarkusJoe/RequestCounter.git
 $ cd RequestCounter
 $ pip3 install -r requirements.txt
 $ python3 app.py 
 ```

## 调用须知
- API支持`GET` 和 `POST` 方法请求
- 最大可以计数`10`位数, 超过则重置
- 可以自定义显示位数默认`7`位数最大`10`位
- 可以自己选择更多的主题只需要加上请求参数: `theme` 再加上想要的主题即可
- 在`theme`请求参数中写入`ls`可以获取所有可选的主题 (来自于`./bin/assets/theme.db`)


# 一些信息
- 使用了Python3.6 的标准库`Sqlite3`进行数据库操作
- 当前支持的主题如下

<details>
foot<br>
gelbooru<br>
gelbooruh<br>
moebooru<br>
moebooruh<br>
g<br>
cripple<br>
blacked<br>
allgirl<br>
rule34<br>
steambanner<br>
lefty<br>
erpg<br>
crewbooru<br>
hgoon<br>
sthg<br>
rfck<br>
lisu<br>
tv<br>
lewd<br>
amibooru<br>
blankatlas<br>
mmballbusting<br>
sss<br>
legolamb<br>
goldengator<br>
r6gdrawfriends<br>
vivi<br>
twifanartsfw<br>
hololive<br>
vglobby<br>
jaypee<br>
melanin<br>
dollstuffing<br>
orb<br>
min<br>
mjg<br>
cloppers<br>
townofgravityfalls<br>
brown<br>
enacdoa<br>
daifuku<br>
straponff<br>
keyofnik<br>
osc<br>
konan<br>
girlsfeet<br>
hybreedsgeneral<br>
sr<br>
mono<br>
riskofrain<br>
neovb<br>
ffsr<br>
</details>


* 仓库总共约`4.12Mb` `theme.db`占用了`4Mb` ...