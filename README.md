# demo-0

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```



## 后端

注：本部分下所有操作均默认在执行`cd backend`后执行

#### 依赖：

开发人员可通过如下命令来打包依赖

```shell
pip install pipreqs
pipreqs . --encoding=utf8 --force
```

通过如下命令来下载依赖

```shell
pip install -r requriements.txt
```

目前已将依赖储存在`requestments.txt`中

#### 操作：

生成数据库(db.sqlite3)：

```python
python manage.py makemigrations
python manage.py migrate
```

创建管理员用户以供进入/admin/直接操作数据库

```
python manage.py createsuperuser
```

运行服务

```python
python manage.py runserver
```

