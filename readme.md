# itchat

[itchat](https://github.com/littlecodersh/ItChat)

# 安装

执行 `pip install -r req.txt` 安装所需要的包。

# 运行

* 直接执行 `./run.sh`;
* 默认使用 sqlite，自动建库建表；
* 第一次登录，会弹出一个二维码，扫码登录；

# 数据库

默认使用 sqlite，数据库文件为 *db.sqlite*

```
CREATE TABLE message_table (
	id INTEGER NOT NULL,
	message TEXT,
	message_type VARCHAR(10),
	message_created VARCHAR(10),
	user_nickname VARCHAR(100),
	dt_created DATETIME,
	PRIMARY KEY (id)
)
```
