# 这是做什么的
没有api key，但是又想部署一个chatgpt，而用access_token，又会过期，手动更新又麻烦，这里就可以提供一个脚本，输入openai的账号密码自动获取access_token，然后部署chatgpt。

> 默认3天更新一次

# 使用方法
```bash
python main.py your_openai_account your_openai_password
```