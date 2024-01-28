import replicate
import os 


# pip install replicate
# export REPLICATE_API_TOKEN=r8_WfeVy2AZMJelm9j3gJIM2JaqYIkkWJi0ObFRk

output = replicate.run(
    "awilliamson10/meta-nougat:872fa99400b0eeb8bfc82ef433aa378976b4311178ff64fed439470249902071",
    input={
        "pdf_link": 'https://drive.google.com/file/d/1-8UlaryILscj5E-Y9VoeHLhAhQnKz_3Y/view?usp=sharing'
    }
)

print(output)

with open('./cache/nougat-api-7A.txt', 'w', encoding='utf-8') as file:
    file.write(output['predictions'])