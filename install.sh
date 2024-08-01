cd /opt
git pull
pip install -i https://mirrors.aliyun.com/pypi/simple/ --no-cache-dir -r requirements.txt
# python3 app.py
python3 -m uvicorn app:app --host 0.0.0.0 --port 8000
# --reload