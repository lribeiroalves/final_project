reinstall:
	pip freeze > uninstall.txt
	pip uninstall -r uninstall.txt -y
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	del uninstall.txt

requirements:
	pip freeze > requirements.txt