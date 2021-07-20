PWD=$(pwd)
if [ ! -d "$PWD/venv" ]; then
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
else
	source venv/bin/activate
fi

source .env
python3 a.py