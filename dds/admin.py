from .models import (
	CashFlowType,
	CashFlowStatus,
	CashFlowCategory,
	CashFlowSubCategory,
	CashFlow
)

from django.contrib import admin


admin.site.register(CashFlow)
admin.site.register(CashFlowType)
admin.site.register(CashFlowStatus)
admin.site.register(CashFlowCategory)
admin.site.register(CashFlowSubCategory)
