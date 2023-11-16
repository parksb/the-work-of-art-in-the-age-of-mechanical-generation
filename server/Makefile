dev:
	make reset && hypercorn main:app --bind 127.0.0.1:8080 --reload

host:
	make reset && hypercorn main:app --bind 0.0.0.0:8080

reset:
	echo 1 > generated_version

fmt:
	black .
