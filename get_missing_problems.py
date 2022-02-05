data_file = open('data.csv')
links_file = open('links.csv')
errors_file = open('errors.txt', 'w')

scraped_links = {}
links = {}

# skip the header line
data_file.readline()
links_file.readline()

for line in data_file.readlines():
    line = line.split(', ')[0].strip('\n')
    if line in scraped_links:
        print(f'{line} found multiple times in scraped data file')
    else:
        scraped_links[line] = True

for line in links_file.readlines():
    line = line.split(', ')[1].strip('\n').strip('/')
    if line in links:
        print(f'{line} found multiple times in scraped links file')
    else:
        links[line] = True

for link in links:
    if link not in scraped_links:
        errors_file.writelines([f'{link}\n'])

print('Done...')
