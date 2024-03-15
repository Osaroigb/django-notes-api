from .models import Note
from rest_framework import status
from .serializers import NoteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

class NoteListCreate(APIView):
    """
    List all notes, or create a new note.
    """
    def get(self, request, format=None):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)

        return Response({
            "message": "Fetched all notes successfully.",
            "data": serializer.data,
            "status": status.HTTP_200_OK
        })


    def post(self, request, format=None):

        serializer = NoteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "message": "Created note successfully.",
                "data": serializer.data,
                "status": status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        
        else:
            return Response({
                "message": "Failed to create note due to validation errors.",
                "data": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):
    """
    Retrieve, update, or delete a note instance.
    """
    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise NotFound(detail="Note not found.", code=404)


    def get(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note)

        return Response({
            "message": "Fetched note successfully.",
            "data": serializer.data,
            "status": status.HTTP_200_OK
        })


    def put(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "message": "Updated note successfully.",
                "data": serializer.data,
                "status": status.HTTP_200_OK
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        note = self.get_object(pk)
        note.delete()

        return Response({
            "message": "Deleted note successfully.",
            "data": {},
            "status": status.HTTP_204_NO_CONTENT
        })