# E-Road

## 前端

注：本部分下所有操作均默认在执行`cd frontend`后执行

### 安装依赖

首先，请您安装node.js与npm，接着执行

```sh
npm install
```

来安装依赖

### 编译得到静态文件

```sh
npm run build
```

### 其它操作

如果您想在本地运行测试，可以使用

```bash
npm run dev
```





## 后端

注：本部分下所有操作均默认在执行`cd backend`后执行

### 安装依赖

`pip install -r requriements.txt `

### 配置邮箱

在`backend/settings`中配置您的邮箱，以供发送邮箱验证码使用

```bash
EMAIL_HOST = 'smtp.qq.com' # 此处为qq邮箱的host，请根据您的情况更改
EMAIL_HOST_USER = '此处填写您的邮箱地址'
EMAIL_HOST_PASSWORD = '此处填写您的邮箱授权码'
EMAIL_PORT = 587 #根据邮箱的不同，端口号也不同，此处为qq邮箱端口号网易系邮箱似乎多为25或465
```

### 生成静态文件

```shell
python manage.py collectstatic
```

### 运行后端

首先，您需要在`uwsgi_conf.ini`中，将`socket = 172.16.26.17:8080`修改为您自己的`私网ip:端口`，之后运行
```shell
uwsgi --ini uwsgi_conf.ini
```
即可运行后端的uwsgi服务。

#### 其它操作：

注：本部分操作主要用于开发人员修改代码进一步开发使用，可根据实际情况操作

生成数据库(db.sqlite3)：

```python
python manage.py makemigrations
python manage.py migrate
```

创建管理员用户以供进入/admin/直接操作数据库

```shell
python manage.py createsuperuser
```

运行服务

```python
python manage.py runserver
```



## 服务器代理配置

在服务器安装`nginx`后，请将`backend/nginx.conf`用作您的nginx配置。例如，如果您的nginx在`/etc/nginx`，可使用`mv backend/nginx.conf /etc/nginx`。

配置`nginx`之后，可运行`systemctl restart nginx`或`systemctl start nginx`启动服务。

#### 注意：

1. 如果您有需要，请备份您原来的`nginx.conf`文件
2. 本项目前端使用了10001端口，后端使用了10002端口，请检查端口是否被占用，以及防火墙是否打开对应的端口(可使用sudo ufw status检查)。
3. 如果您使用的是阿里云等在网上购买的服务器，有可能云服务器提供商会为您的服务器提供防护，从而导致端口无法从外部访问，这需要您在云服务器供应商提供的控制台上修进行相关设置。