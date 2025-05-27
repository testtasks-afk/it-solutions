from django.core.exceptions import ValidationError

class CategoryTypeValidator:
	@staticmethod
	def validate(type_, category, sub_category):
		if category.type != type_:
			raise ValidationError(
				message={
					"category": "выбранная категория не принадлежит к типу"
				}
			)

		if sub_category.category != category:
			raise ValidationError(
				message={
					"sub_category": "выбранная подкатегория не принадлежит к категории"
				}
			)