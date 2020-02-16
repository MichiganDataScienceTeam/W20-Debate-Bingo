import pandas as pd

def read_data():
    debates = pd.read_csv('data/june1_transcript.csv')
    debates['month'] = 'june'
    df = pd.read_csv('data/june2_transcript.csv')
    df['month'] = 'june'
    debates = debates.append(df)
    df = pd.read_csv('data/july1_transcript.csv')
    df['month'] = 'july'
    debates = debates.append(df)
    df = pd.read_csv('data/july2_transcript.csv')
    df['month'] = 'july'
    debates = debates.append(df)
    df = pd.read_csv('data/september_transcript.csv')
    df['month'] = 'september'
    debates = debates.append(df)
    df = pd.read_csv('data/october_transcript.csv')
    df['month'] = 'october'
    debates = debates.append(df)
    df = pd.read_csv('data/november_transcript.csv')
    df['month'] = 'november'
    debates = debates.append(df)
    df = pd.read_csv('data/december_transcript.csv')
    df['month'] = 'december'
    debates = debates.append(df)
    df = pd.read_csv('data/january_transcript.csv')
    df['month'] = 'january'
    debates = debates.append(df)
    df = pd.read_csv('data/february_transcript.csv')
    df['month'] = 'february'
    debates = debates.append(df)
    debates = debates[['name', 'text', 'month', 'time']]
    return debates


def standardize_names(debates):
    debates.name[debates.name.isin(['Senator Warren', 'E. Warren', 'Elizabeth W.', 'Elizabeth W', 'Elizabeth Warre', 'Elizabeth Warren'])] = 'Warren'
    debates.name[debates.name.isin(['Cory Booker', 'Senator Booker'])] = 'Booker'
    debates.name[debates.name.isin(['Amy Klobuchar', 'Amy Klobachar', 'Sen Klobuchar'])] = 'Klobuchar'
    debates.name[debates.name.isin(['Mayor de Blasio', 'Bill de Blasio', 'Bill De Blasio'])] = 'de Blasio'
    debates.name[debates.name.isin(['Yang', 'Andrew Yang'])] = 'Yang'
    debates.name[debates.name.isin(['Bernie Sanders'])] = 'Sanders'
    debates.name[debates.name.isin(['Senator Bennet', 'Bennett', 'Michael Bennet'])] = 'Bennet'
    debates.name[debates.name.isin(['Kirsten G.', 'Gillibrand', 'Kristen Gillibr'])] = 'Gillibrand'
    debates.name[debates.name.isin(['Kamala Harris'])] = 'Harris'
    debates.name[debates.name.isin(['Marianne W.', 'M. Williamson', 'Marianne Willia', 'Ms. Williamson'])] = 'Williamson'
    debates.name[debates.name.isin(['Julian Castro', 'Sec. Castro', 'Juliu00e1n Castro'])] = 'Castro'
    debates.name[debates.name.isin(['Joe Biden', 'Joe Biden '])] = 'Biden'
    debates.name[debates.name.isin(['John Delaney'])] = 'Delaney'
    debates.name[debates.name.isin(['John H.', 'John H', 'John Hickenloop', 'J. Hickenlooper'])] = 'Hickenlooper'
    debates.name[debates.name.isin(['Tom Steyer'])] = 'Steyer'
    debates.name[debates.name.isin(['Eric Stalwell', 'Eric Swalwell'])] = 'Swalwell'
    debates.name[debates.name.isin(['Pete Buttigieg', 'Mayor Buttigieg'])] = 'Buttigieg'
    debates.name[debates.name.isin(['Tulsi Gabbard'])] = 'Gabbard'
    debates.name[debates.name.isin(['Steve Bullock'])] = 'Bullock'
    debates.name[debates.name.isin(['Jay Inslee'])] = 'Inslee'
    debates.name[debates.name.isin(['Tim Ryan'])] = 'Ryan'
    debates.name[debates.name.isin(['Beto O’Rourke', 'Beto O\'Rourke'])] = 'O\'Rourke'
    candidates = ['Warren', 'Booker', 'Klobuchar', 'de Blasio', 'Yang', 'Sanders', 'Bennet', 'Gillibrand', 'Harris', 'Williamson', 'Castro', 'Biden', 'Swalwell', 'Buttigieg', 'Gabbard', 'Hickenlooper', 'Steyer', 'Bullock', 'Inslee', 'Ryan', 'O\'Rourke', 'Delaney']
    debates.name[~debates.name.isin(candidates)] = 'Non-candidate'
    return debates

def convert_data(debates):
    debates.to_csv('data/transcripts_cleaned.csv', index = False)

def main():
    debates = read_data()
    standardize_names(debates)
    convert_data(debates)

if __name__ == '__main__':
    main()
