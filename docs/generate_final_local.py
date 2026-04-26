import os

docs_dir = r'c:\Users\david\WebstormProjects\Project-report\docs'
front_matter_dir = os.path.join(docs_dir, 'front-matter')

files = [
    os.path.join(front_matter_dir, '01-title-page.md'),
    os.path.join(front_matter_dir, '02-version-control-log.md'),
    os.path.join(front_matter_dir, '03-collaboration-insights.md'),
    os.path.join(front_matter_dir, '04-table-of-contents.md'),
    os.path.join(front_matter_dir, '05-student-outcomes.md'),
    os.path.join(front_matter_dir, '06-abstract.md'),
    os.path.join(docs_dir, '10-chapter-01.md'),
    os.path.join(docs_dir, '11-chapter-02.md'),
    os.path.join(docs_dir, '12-chapter-03.md'),
    os.path.join(docs_dir, '13-chapter-04.md'),
    os.path.join(docs_dir, '14-chapter-05.md'),
    os.path.join(docs_dir, '15-chapter-06.md'),
    os.path.join(docs_dir, '99-bibliography.md'),
]

master_path = os.path.join(docs_dir, 'Reporte-Final-Buildline-AV1.md')

with open(master_path, 'w', encoding='utf-8') as master:
    for f in files:
        if os.path.exists(f):
            with open(f, 'r', encoding='utf-8') as source:
                content = source.read()
                content = content.replace('{-}', '')
                content = content.replace('../assets/', 'assets/')
                content = content.replace('./assets/', 'assets/')
                master.write(content)
                master.write('\n\n<div class="page-break"></div>\n\n')

print("Master file generated: " + master_path)
