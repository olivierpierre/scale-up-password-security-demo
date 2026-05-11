all: container-build slides

slides:
	make -C slides

container-build:
	docker build -t olivierpierre/scale-up-password-demo .

container-run: container-build
	docker run -it olivierpierre/scale-up-password-demo

container-push: container-build
	docker login
	docker push olivierpierre/scale-up-password-demo