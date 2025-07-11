titles = ['The Concrete Shell / UA Lab (Urban Architectural Collaborative)',
 'Bunkie on the Hill / Dubbeldam Architecture + Design',
 'Patios House / studio mk27',
 'Mureli House / Makhno Studio',
 'Hertogensite Residences / David Chipperfield Architects',
 'Remembering 9/11: The Story of Rebuilding the World Trade Center',
 'Terrazza Biandrà Elevated Plaza / Park Associati',
 'Shigeru Ban Receives the 2024 Praemium Imperiale for Architecture',
 'Dehkadeh Iwan House / Super Void Space',
 'Azerbaijan Pavilion at Expo 2025 Osaka, Designed by Bellprat Partner, Leads Visitors on a Journey Through Traditions',
 'How to Express Design Ideas with Artistic Visual Modes',
 'A Cultural Complex in Iraq and an Urban Cloister in India: 10 Unbuilt Masterplans Submitted by the ArchDaily Community',
 'Ecole du Zenith / Pelletier De Fontenay',
 'Facette Bordeaux Workspace / Studioninedots',
 'Asahi no Mori Internal Medicine and Gastroenterology Clinic / TSC Architects',
 'Avant Bakery / oftn studio',
 'Cesariny Exhibition / fala',
 'Alibaba Shanghai Campus / Foster + Partners',
 'OrigaMI Apartment / A I M']

titles = [i for i in titles if '/' in i]
print(titles)

titles_dict = {}
for i in titles:
    sub_list = i.split('/')
    x = sub_list[0]
    y = sub_list[1]
    titles_dict[x] = y
print(titles_dict)