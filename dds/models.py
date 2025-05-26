from django.core.validators import MinValueValidator
from django.db import models

class CashFlowCategory(models.Model):
	name = models.CharField(max_length=50)
	verbose_name = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.verbose_name if self.verbose_name else self.name


class CashFlowSubCategory(models.Model):
	name = models.CharField(max_length=50)
	verbose_name = models.CharField(max_length=50, null=True)
	category = models.ForeignKey(to=CashFlowCategory, on_delete=models.CASCADE)

	def __str__(self):
		return self.verbose_name if self.verbose_name else self.name


class CashFlowStatus(models.Model):
	name = models.CharField(max_length=50)
	verbose_name = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.verbose_name if self.verbose_name else self.name


class CashFlowType(models.Model):
	name = models.CharField(max_length=50)
	verbose_name = models.CharField(max_length=50, null=True)

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
	comment = models.TextField(null=True)

	def __str__(self):
		return f'операция {self.type} в категории {self.category} на сумму {self.amount}'

