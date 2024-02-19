import re 
 
with open('ansibleJobEvent.json') as ansible_json:
  ansible_job_event_data = ansible_json.read()

regex = r"(\"task\"):\"(.*?)\""

final_matches = list()
matches = re.finditer(regex, ansible_job_event_data, re.MULTILINE)
for matchGroup, match in enumerate(matches, start=1):
    match = match.group()
    if len(match) > 255:
       final_matches.append(match)

final_match_set = set(final_matches)
final_match_list = list(final_match_set)
number = 0
for eachMatch in final_match_list:
    number = number + 1
    print(f"{number}:\r\n{eachMatch} is \033[1mgreater than 255 characters\033[0m. \033[91m\033[1mCHARACTER COUNT: {len(eachMatch)}\033[0m\r\n")

ansible_json.close()        
