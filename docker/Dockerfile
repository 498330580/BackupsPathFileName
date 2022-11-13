# 基础版本python3.10
FROM python:alpine3.10
# 创建工作目录
RUN mkdir -p /app
RUN mkdir -p /backup

# 指定语言，防止中文日志乱码
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8
ENV TIME 60

# 指定pip源，并更新pip
COPY ./docker/pip.conf /root/.pip/pip.conf
RUN pip install --upgrade pip

# 添加项目文件到app目录
COPY . /app

# 添加定时任务
COPY ./docker/python-cron /etc/cron.d/python-cron
RUN chmod 0644 /etc/cron.d/python-cron
RUN crontab /etc/cron.d/python-cron
# RUN touch /app/logs/get_xiaosuo.log

# 用于指定持久化目录（指定此目录可以被挂载出去）
VOLUME ['/app/data', "/app/logs"]

# 指定工作目录
WORKDIR /app

# 运行
CMD [ "python3", "/app/main.py" ]