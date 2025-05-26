from django.contrib import admin
from .models import (
	CashFlowType,
	CashFlowStatus,
	CashFlowCategory,
	CashFlowSubCategory,
	CashFlow
)

admin.site.register(CashFlow)
admin.site.register(CashFlowType)
admin.site.register(CashFlowStatus)
admin.site.register(CashFlowCategory)
admin.site.register(CashFlowSubCategory)
