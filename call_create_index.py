from document_gpt.helper.index import create_indexes

file_path = 'nutri_hydro_intro.pdf'

result = create_indexes(file_path)

print(result)
