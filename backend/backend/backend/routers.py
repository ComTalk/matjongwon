# Database Router
class MatjongwonRouter:
    """
    A router to control all database operations on models in the 
    places and like applications.
    """

    #route_app_labels = {'places'}
    route_app_labels = {'places', 'like', 'users'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'matjongwon'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels: 
            return 'matjongwon'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'matjongwon'
        return db == 'default'
