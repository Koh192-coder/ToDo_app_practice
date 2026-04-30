FROM python:3.14-slim

# 作業ディレクトリを作成 一般的には/appという名称を使う
WORKDIR /app

# .(現在のディレクトリ)を/appにコピー
# .はDockerfileがある場所のディレクトリのこと
COPY . /app


# -rはpipのオプション -rがないとpipはパッケージ名だと解釈する
RUN pip install -r requirements.txt


CMD [ "uvicorn","main:app","--reload","--host","0.0.0.0" ]