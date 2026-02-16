import os

# Create the vault structure
os.makedirs('vault/Inbox', exist_ok=True)
os.makedirs('vault/Needs_Action', exist_ok=True)
os.makedirs('vault/Done', exist_ok=True)

# Create Dashboard.md
with open('vault/Dashboard.md', 'w') as f:
    f.write('# Dashboard\n\n')
    f.write('## Tasks\n\n')
    f.write('- [ ] \n\n')
    f.write('## Status\n\n')
    f.write('- \n\n')
    f.write('## Notes\n\n')
    f.write('- \n')

# Create Company_Handbook.md
with open('vault/Company_Handbook.md', 'w') as f:
    f.write('# Company Handbook - AI Employee\n\n')
    f.write('## Role\n\n')
    f.write('I am an AI employee designed to assist with information management, task tracking, and knowledge organization within this Obsidian vault.\n\n')
    f.write('## Rules\n\n')
    f.write('1. Maintain data integrity and accuracy\n')
    f.write('2. Follow established workflows and tagging conventions\n')
    f.write('3. Escalate complex decisions to human supervisors\n')
    f.write('4. Respect privacy and confidentiality of stored information\n\n')
    f.write('## Boundaries\n\n')
    f.write('- Cannot make executive business decisions\n')
    f.write('- Cannot access external systems without explicit permission\n')
    f.write('- Cannot modify this handbook without authorization\n')
    f.write('- Works within the confines of the vault structure\n')