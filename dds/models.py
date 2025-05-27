from django.core.validators import MinValueValidator
from django.db import models

from dds.services import CategoryTypeValidator


class CashFlowType(models.Model):
	name = models.CharField(max_length=50)
	verbose_name = models.CharField(max_length=50, blank=True)

	class Meta:
		verbose_name = "Тип"
		verbose_name_plural = "Типы"

	def __str__(self):
		return self.verbose_name if self.verbose_name else self.name


class CashFlowCategory(models.Model):
	name = models.CharField(max_length=50)
	verbose_name = models.CharField(max_length=50, blank=True)
	type = models.ForeignKey(to=CashFlowType, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"

	def __str__(self):
		return self.verbose_name if self.verbose_name else self.name


class CashFlowSubCategory(models.Model):
	name = models.CharField(max_length=50)
	verbose_name = models.CharField(max_length=50, blank=True)
	category = models.ForeignKey(to=CashFlowCategory, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Подкатегория"
		verbose_name_plural = "Подкатегории"

	def __str__(self):
		return self.verbose_name if self.verbose_name else self.name


class CashFlowStatus(models.Model):
	name = models.CharField(max_length=50)
	verbose_name = models.CharField(max_length=50, blank=True)

	class Meta:
		verbose_name = "Статус"
		verbose_name_plural = "Статусы"

	def __str__(self):
		return self.verbose_name if self.verbose_name else self.name


class CashFlow(models.Model):
	status = models.ForeignKey(to=CashFlowStatus, on_delete=models.CASCADE)
	type = models.ForeignKey(to=CashFlowType, on_delete=models.CASCADE)
	category = models.ForeignKey(to=CashFlowCategory, on_delete=models.CASCADE)
	sub_category = models.ForeignKey(to=CashFlowSubCategory, on_delete=models.CASCADE)

	date = models.DateField(auto_now_add=True)
	amount = models.DecimalField(
		max_digits=10,
		decimal_places=2,
		validators=[MinValueValidator(0.00)]
	)
	comment = models.TextField(blank=True)

	class Meta:
		verbose_name = "Движение Денежных Средств"
		verbose_name_plural = "Движения Денежных Средств"

	def clean(self):
		super().clean()

		CategoryTypeValidator.validate(
			self.type,
			self.category,
			self.sub_category
		)

	def save(self, *args, **kwargs):
		self.full_clean()
		super().save(*args, **kwargs)

	def __str__(self):
		return f'операция {self.type} в категории {self.category} на сумму {self.amount}'

