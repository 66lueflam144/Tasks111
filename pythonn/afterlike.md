# Python 爬虫
>原理：
（1）发起请求：通过向HTTP协议向目标站点发送请求（一个request），然后等待目标站点服务器的响应。
（2）获取响应内容：服务器正常响应，将得到一个response。response的内容便是所要获取的页面内容，响应的内容有HTML，Json串，二进制数据（图片视频）等等。
（3）解析内容：得到的内容是HTML，可以用正则表达式、网页解析库进行解析；Json，可以直接转为Json对象解析；二进制数据，可以保存或者进一步的处理。
（4）保存数据：数据解析完成后，将保存下来。既可以存为文本文档，亦可以存到数据库中。
 
---
&emsp;:grinning:<a href="https://zhuanlan.zhihu.com/p/355797583">a good thing</a>

---

## python爬出：
- （1）安装requests库和BeatifulSoup库。
- （2）获取爬虫所需的header和cookie。
- (3)获取网页。
- （4）分析得到的信息，简化地址。
- (5)爬取内容，清洗数据。
- 