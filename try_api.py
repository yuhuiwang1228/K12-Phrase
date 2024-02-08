import replicate
import os 


# pip install replicate
# export REPLICATE_API_TOKEN=r8_WfeVy2AZMJelm9j3gJIM2JaqYIkkWJi0ObFRk
url = 'https://s29.q4cdn.com/175625835/files/doc_downloads/test.pdf'
output = replicate.run(
    "awilliamson10/meta-nougat:872fa99400b0eeb8bfc82ef433aa378976b4311178ff64fed439470249902071",
    input={
        "pdf_link": url
    }
)

print(output)

with open('./cache/nougat-api-7A.txt', 'w', encoding='utf-8') as file:
    file.write(output['predictions'])