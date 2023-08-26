from rest_framework.views import APIView
from rest_framework.response import Response
from docxtpl import DocxTemplate
from io import BytesIO
from django.template import Template, Context
from .models import DocumentTemplate

class GenerateDocumentView(APIView):
    def post(self, request, format=None):
        try:
            template_id = request.data.get('template_id')
            data = request.data.get('data')
            format = request.data.get('format', 'text_plain')

            template = DocumentTemplate.objects.get(id=template_id)
            
            print("Hola", template.template_text )
            print("holiii")
            if template.template_text == "":
                print(1)
            else:
                print(2)

            template_text = template.template_text

            t = Template(template_text)
            context = Context(data)
            document_content = t.render(context)

            if format == 'text_plain':
                return Response({'document': document_content})

            elif format == 'docx':
                doc = DocxTemplate(BytesIO())
                doc = DocxTemplate(BytesIO(document_content.encode('utf-8')))
                doc_buffer = BytesIO()
                doc.save(doc_buffer)
                doc_buffer.seek(0)
                return Response(doc_buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                print(1)
                doc = DocxTemplate(BytesIO())
                print(2)
                doc = DocxTemplate(BytesIO(document_content.encode('utf-8')))
                print(str(doc))
                doc_buffer = BytesIO()
                print(4)
                doc.save(doc_buffer)
                print(5)
                doc_buffer.seek(0)
                print(6)
                return Response(doc_buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

            else:
                return Response({'error': 'Invalid format'}, status=400)

        except Exception as e:
            return Response({'error': str(e)}, status=500)

"""         uploaded_file = request.FILES.get('file')  
            print(uploaded_file)
            if uploaded_file is not None:
                if uploaded_file.content_type == 'application/json':
                    file_content = uploaded_file.read()  
                    input_data = json.loads(file_content.decode('utf-8'))
                    print(1)

                elif uploaded_file.content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
                    doc = Document(uploaded_file)
                    texto = "\n".join([p.text for p in doc.paragraphs])
                    input_data = json.loads(texto)
                    print(2)
            else:
                input_data = request.data
                print(3)
                      
            template_id = input_data.get('template_id')
            data = input_data.get('data')
            format = input_data.get('format', 'text_plain')
            
            template = DocumentTemplate.objects.get(id=template_id)
            print(template)
            # MODELO POR TEXTO 
            if template.template_document == "":
                template_text = template.template_text
            # MODELO POR DOCX O TXT
            else:
                file_extension = str(template.template_document).split(".")
                if file_extension[1] == 'docx':
                    doc2 = Document(template.template_document)
                    template_text =  "\n".join([p.text for p in doc2.paragraphs])
                elif file_extension[1] == 'txt':
                    template_text = template.template_document.read().decode('utf-8')

            t = Template(template_text)
            context = Context(data)
            document_content = t.render(context)
            
            if format == 'text_plain':
                return Response({'document': document_content})

            elif format == 'docx':
                doc = Document()
                doc.add_paragraph(document_content)
                doc_buffer = io.BytesIO()
                doc.save(doc_buffer)
                doc_buffer.seek(0)
                
                response = StreamingHttpResponse( 
                    streaming_content=doc_buffer,  
                    content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                )

                response['Content-Disposition'] = 'attachment;filename=Test.docx'
                response["Content-Encoding"] = 'UTF-8'

                return response
            else:
                return Response({'error1': 'Invalid format'}, status=400)
"""

"""OTRA FORMA 
for a in data:
                    # RENDERIZACIÓN
                    env = Environment()
                    tmpl = env.from_string(template)
                    document_content = tmpl.render(a)
                    #SALIDA POR TEXTO PLANO
                    if format == 'text_plain':
                        response1.append({'document': document_content})
                        respuesta = Response(response1)
                    #SALIDA POR DOCX
                    elif format == 'docx':
                        doc = Document()
                        doc.add_paragraph(document_content)

                        doc_buffer = io.BytesIO()
                        doc.save(doc_buffer)
                        doc_buffer.seek(0)

                        response = StreamingHttpResponse( 
                            streaming_content=doc_buffer,
                            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                        )
                        #TITULO
                        response['Content-Disposition'] = 'attachment;filename=Test.docx'
                        response["Content-Encoding"] = 'UTF-8'

                        #url = "C:\Users\danii\Downloads"

                        #responses = requests.get(url)
                        
                        if response.status_code == 200:
                            with open("Test"+str(cont)+".docx", "wb") as f:
                                cont = cont + 1
                                doc.save(f)
                                doc6 = bytes(document_content, 'utf-8')
                                f.write(doc6)
                                for chunk in response1.streaming_content:
                                    f.write(chunk)

                            respuesta = response
                        else:
                            respuesta = print(f"Error al descargar el archivo: {response.status_code}")
                        
                        
                    else:
                        return Response({'error1': 'Invalid format'}, status=400)
                    
                return respuesta
            return Response({
                'message': 'ha ocurrido un problema con serializer del producto',
                'error':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error2': str(e)}, status=500)

"""