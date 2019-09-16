from django.conf import settings

DATABASES_MAPPING = settings.DATABASES_APPS_MAPPING

dbname = 'mysql'

class DatabaseAppsRouter:
	def db_for_read(self, model, **hints):
		if model._meta.app_label == 'polls':
			return dbname

		return None

	def db_for_write(self, model, **hints):
		if model._meta.app_label == 'polls':
			return dbname

		return None

	def allow_relation(self, obj1, obj2, **hints):
		if obj1._meta.app_label == 'polls' or obj2._meta.app_label == 'polls':
			return True

		return None

	def allow_migrate(self, db, app_label, model_name=None, **hints):
		if app_label == 'polls':
			return db == dbname

		return None
