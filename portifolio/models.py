from django.db import models

class Techs(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='midia/projects/')
    alt = models.CharField(max_length=150, blank=True, null=True)

    techs = models.ManyToManyField(Techs, related_name='projects')

    demo_link = models.URLField(blank=True, null=True)
    code_link = models.URLField(blank=True, null=True)

    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()

    photo = models.ImageField(upload_to='midia/profile/')
    cv = models.FileField(upload_to='midia/profile/')

    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    email = models.EmailField()

    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    titulo = models.CharField(max_length=100)
    aluno = models.CharField(max_length=100)
    data = models.DateField()
    code = models.CharField(max_length=50, blank=True, null=True)
    cv = models.FileField(upload_to='midia/certificate/')

    def __str__(self):
        return f"{self.titulo} - {self.aluno}"


class Activity(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Experience(models.Model):
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    periodo = models.CharField(max_length=50)
    descricao = models.TextField()

    atividades = models.ManyToManyField(
        Activity,
        related_name='experiences',
        blank=True
    )

    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"
