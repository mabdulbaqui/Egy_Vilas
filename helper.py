import pandas as pd 
def transform_d(data, column_name, categories, is_ordinal = False, asserted = True):
    
    df = data.copy(deep = True)
    
    if asserted:
        assert df[column_name].apply(lambda x: x in categories).all()
    
    column_series = df[column_name]
    df.drop(column_name, axis = 1, inplace = True)
    
    if is_ordinal:

        d = {x : i + 1 for i, x in enumerate(categories)}
        column_series.replace(d, inplace = True)
        
        df[column_name] = column_series
    
    else:
        
        columns = [f'{column_name}: {x}' for x in categories]
        temp_df = column_series.apply(lambda x: pd.Series([int(y == x) for y in categories]))
        temp_df.columns = columns
        
        df = df.join(temp_df)
        
    return df
        
        
def transform_c(data, column_name):
    
    df = data.copy(deep = True)
    
    column_series = df[column_name]
    df.drop(column_name, axis = 1, inplace = True)
    df[column_name] = column_series
    
    return df
    
    
def transform(data, column_name, categories = None, is_ordinal = False, asserted = True):

    if categories is None:
        
        return transform_c(data, column_name)
        
    return transform_d(data, column_name, categories, is_ordinal, asserted)
    

def transform_features(X_df):    
    #Column: manufacturer
    
    categories = ['Sheikh Zayed، Giza', 'Rehab City، Cairo', 'New Cairo - El Tagamoa, Cairo', 'Shorouk City، Cairo', 'Madinaty، Cairo', 'New Cairo - El Tagamoa، Cairo', '6th of October، Giza', 'Madinaty, Cairo', 'Mokattam, Cairo', '6th of October, Giza', 'Sheikh Zayed, Giza', 'Dokki، Giza', 'New Capital City، Cairo', 'Mostakbal City، Cairo', 'North Coast، Matruh', 'Heliopolis، Cairo', 'Borg al-Arab، Alexandria', 'Mokattam، Cairo', 'Zohour District، Port Said', 'Rehab City, Cairo', 'Hadayek al-Ahram، Giza', 'Obour City، Cairo', 'Borg al-Arab, Alexandria', 'Hurghada, Red Sea', 'Maadi، Cairo', 'Hadayek 6th of October، Giza', 'Ain Sukhna، Suez', 'Hurghada، Red Sea', 'New Damietta، Damietta', 'Ismailia City، Ismailia', 'Giza District، Giza', 'Haram، Giza', 'Agami، Alexandria', '10th of Ramadan، Sharqia', 'New Heliopolis، Cairo', 'Shorouk City, Cairo', 'West Somid، Giza', 'Alamein، Matruh', 'Sharm al-Sheikh، South Sinai', 'North Coast, Matruh', 'Nasr City، Cairo', 'Badr City، Cairo', 'New Capital City, Cairo', 'Downtown Cairo، Cairo', 'Ain Shams، Cairo', 'Mostakbal City, Cairo', 'New Minya، Minya', 'Marsa Matrouh، Matruh', 'Mansuriyya، Giza', 'Kafr Abdo، Alexandria', 'Tersa، Giza', 'Abu Talat، Alexandria', 'Ras Sedr، South Sinai', '15 May City، Cairo', 'Helmeyat El Zaytoun، Cairo', 'Mansura، Dakahlia', 'Heliopolis, Cairo', 'Maadi, Cairo', 'Zahraa Al Maadi، Cairo', 'Ain Sukhna, Suez', 'Nasr City, Cairo', 'Obour City, Cairo']
    

    
    df = transform(data = X_df,
                   column_name = 'location', 
                   categories = categories, 
                   is_ordinal = False,
                   asserted = True)
    
    ############################################
    
    #Column: condition
    # drop_first=flase 
    df = transform(data = df, 
                   column_name = 'Type', 
                   categories = ['Twin House', 'Town House'], 
                   is_ordinal = False,
                   asserted = False)
    
    ############################################
    
    #Column: cylinders
    
    df = transform(data = df, 
                   column_name = 'Payment Option', 
                   categories = ['Cash', 'Installment'], 
                   is_ordinal = False,
                   asserted = False)
    
    ############################################
    
    #Column: fuel
    
    categories = ['Lake West', 'not_in_Compound', 'Hyde Park New Cairo', 'Al Rabwa', 'Rehab City', 'EL Patio Prime', 'Madinaty', 'Village West', 'Beverly Hills', 'Villette', 'Swan Lake', 'Sun Capital', 'Zizinia Gardens', 'EL Patio 5', 'Layan', 'Taj City', 'Uptown Cairo', 'EL Patio 6', 'El Karma 4', 'El Patio', 'Mountain View Chillout Park', 'Royal City', 'Mena Garden City', 'Al Yasmine', 'Royal Meadows', 'Sodic Westown', 'El Karma 2', 'Allegria', 'Sama', 'New Giza', 'Midtown Sky', 'Vinci', 'IL Bosco', 'Blue Vert', 'Midtown Solo', 'Kayan', 'Jedar', 'Stella Compounds', 'Badya Palm Hills', 'Etapa', 'Mountain View iCity', 'Azzar', 'O West', 'Etoile de Ville', 'Sarai', 'Maxim Country Club', 'Palm Hills Katameya', 'Palm Hills Katameya Extension', 'Dyar', 'Moon Hillls', 'La Vida', 'The Square', 'Grand Residence', 'Katameya Breeze', 'Al Diyar', 'Joulz', 'Palm hills golf extension', 'Cairo Festival City', 'Villino', 'El Karma', 'Mivida', 'EL Patio ORO', 'Palm hills golf views', 'Kattameya Residence', 'Al Burouj', 'Les Rois', 'Tawny', 'Atrio', 'Eastown', 'La Vista City', 'Kattameya Gardens', '2020 Compound', 'Marina City', 'The Crown', 'EL Patio Casa', 'Rayos', 'Porto October', 'Alma', 'Sodic East', 'Mountain View - October Park', 'Zayed 2000', 'Concord Gardens', 'Cleopatra Palace', 'Gardenia', 'Dreamland', 'De Joya', 'Palm Parks', 'Silva', 'Mountain View 2', 'Ourika', 'Aswar', 'Trio Gardens', 'Grand Heights', 'Belle Vie', 'Keeva', 'Palm Hills New Cairo', 'El Reef El Orouby', 'Bloomfields', 'Fountain Park', 'VGK', 'Karma Residence', 'Zayed Dunes', 'Pyramids Walk', 'Monte Napoleon', 'Cleopatra Square', 'Leena Springs', 'Bellagio', 'Fifth Square', 'Golden Heights', 'Zed East', 'River Walk', 'Casa Verde', 'Moon Valley', 'La Rose', 'Meadows Park', 'Jeera', 'Palm Valley', 'Al Maqsad', 'Green 4', 'Nakheel', 'Bamboo Palm Hills', 'Greens', 'Hadaba', 'The Estates', 'Mountain View 1', 'The MarQ', 'Not in Compound', 'Divina Gardens', 'Creek Town', 'District 5 Compound', 'Stone Park', 'Mountain View Hyde Park', 'La Terra', 'Cairo Gate', 'Rock Ville', 'Katameya Dunes', 'Emerald Park', 'May Fair', 'Lake View', 'Hayah Residence', 'Fleur De Ville', 'IL Bosco City', 'Zayed Regency', 'Al Solaimaneyah Golf City', 'Woodville', 'Gardenia Springs', 'Katameya Hills', 'Concordia', 'Villar Residence', 'L’Avenir', 'EL Patio 2', 'La Verde', 'Green Square', 'Seasons', 'Katameya Heights']
    
    df = transform(data = df, 
                   column_name = 'Compound', 
                   categories = categories,
                   is_ordinal = False,
                   asserted = True)
    

    
    df = transform(data = df, 
                   column_name = 'Delivery Term', 
                   categories = ['Finished', 'Semi Finished', 'Not Finished'],
                   is_ordinal = False,
                   asserted = False)
    
    
    ############################################
    
        
    df = transform(data = df, 
                   column_name = 'Delivery Date', 
                   categories = ['Ready to move', 'soon', '2025', '2023', '2024', 'within 6 months', '2022'],
                   is_ordinal = False,
                   asserted = True)
    
    return df