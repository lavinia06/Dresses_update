from faker import Faker

if __name__ == '__main__':

    fake = Faker()

    batch_size = 10
    with open('dresses.sql', 'w') as file:

        # sql = "TRUNCATE TABLE dresses_brand RESTART IDENTITY CASCADE;\n \
        #         TRUNCATE TABLE dresses_dress RESTART IDENTITY CASCADE;\n \
        #         TRUNCATE TABLE dresses_redcarpetpresentation RESTART IDENTITY CASCADE;\n \
        #         TRUNCATE TABLE dresses_showevent RESTART IDENTITY CASCADE;\n \
        #         "

        #file.write(sql + "\n")

        for i in range(0, 10000, 100):
            brands = []
            for j in range(i, i + 2):
                brand_fondator = fake.name()
                brand_name = fake.name()
                brand_rank = fake.random_element(elements=("affordable", "expensive", "cheap", "very expensive"))
                nr_models = fake.random_int(min=10, max=30)
                brands.append(f"('{brand_fondator}', '{brand_name}', '{brand_rank}', '{nr_models}')")
            data = f"INSERT INTO dresses_brand (brand_fondator, brand_name, brand_rank, nr_models) VALUES {','.join(brands)};"
            file.write(data + "\n")


        for i in range(0, 10000, 100):
            dresses = []
            for j in range(i, i + 2):
                name = fake.random_element(elements=("wedding dress", "vacation dress", "club dress", "summer dress", "mini dress"))
                description = fake.text(max_nb_chars=50).replace('\n',' ')
                color = fake.random_element(elements=("white", "black", "pink", "red"))
                model_wearing = fake.name()
                price = fake.random_int(min=2000, max=10000)
                brand_id = fake.random_int(min=1, max=20)
                dresses.append(f"('{name}', '{description}', '{color}', '{model_wearing}', '{price}', '{brand_id}')")
            data = f"INSERT INTO dresses_dress (name, description, color, model_wearing, price, brand_id_id) VALUES {','.join(dresses)};"
            file.write(data + "\n")



        for i in range(0, 10000, 1000):
            presentations = []
            for j in range(1, i+2):
                holder = fake.name()
                city_name = fake.random_element(elements=("Constanta", "Bistrita", "Cluj", "Parva", "Bucuresti", "Timisoara", "Oradea"))
                special_guest = fake.name()
                event_name = fake.name()
                nr_guests = fake.random_int(min=10, max=30000)
                presentations.append(f"('{holder}', '{city_name}', '{special_guest}', '{event_name}', '{nr_guests}')")
            data = f"INSERT INTO dresses_redcarpetpresentation (holder, city_name, special_guest, event_name, nr_guests) VALUES {','.join(presentations)};"
            file.write(data + "\n")


        for i in range(0, 10000, 100):
            shows = []
            for j in range(1, 1+1):
                pieces = fake.random_int(min=1, max=10000)
                show_date = fake.date()
                show_popularity = fake.random_int(min=1, max=5)
                dress = fake.random_int(min=1, max=19)
                presentation = fake.random_int(min=1, max=19)
                shows.append(f"('{pieces}', '{show_date}', '{show_popularity}', '{dress}', '{presentation}')")
            data = f"INSERT INTO dresses_showevent (pieces, show_date, show_popularity, dress_id, presentation_id) VALUES {','.join(shows)};"
            file.write(data + "\n")

