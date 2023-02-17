from rest_framework.permissions import BasePermission
from comments.models import Comment

class IsOwnerOrReadAndCreateOnly(BasePermission):
    def hast_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            id_comment = view.kwargs['pk'] #obtengo el id del comentario
            comment = Comment.objects.get(pk=id_comment) #obtengo los datos de ese comentario

            id_user = request.user.pk #obtengo el id que esta ejecutando la peticion
            id_user_comment = comment.user_id #obtengo el id del propietario del comentario

            if id_user == id_user_comment:
                return True
            return False
