import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as m_lines

from collections import Counter


def create_diagram() -> None:
    with open(file='vacancy.csv', mode='r', encoding='utf-8') as file:
        vacancy: csv.DictReader = csv.DictReader(file, delimiter=',')

        skills = Counter(
            ''.join(skill.strip().replace(' / ', '')).capitalize() for row in vacancy if row['key_skills'] for skill in
            row['key_skills'].split(',')).most_common(15)

    df = pd.DataFrame(skills, columns=['key_skills', 'count'])

    fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
    ax.hlines(y=df.index, xmin=0, xmax=df['count'].max() + 10, color='gray', alpha=0.7, linewidth=1,
              linestyles='dashdot')
    ax.scatter(y=df.index, x=df['count'], s=75, color='firebrick', alpha=1)
    ax.plot(df['count'], df.index, color='red', linestyle='--')

    ax.set_yticks(df.index)
    ax.set_yticklabels(df['key_skills'])
    ax.invert_yaxis()

    lines = [m_lines.Line2D([], [], color='firebrick', marker='o', markersize=10, label=f'{skill}: {count}') for
             skill, count
             in zip(df['key_skills'], df['count'])]
    ax.legend(handles=lines, loc='lower right', title='Skills')

    ax.set_title('Top 15 professional skills',
                 fontdict={'size': 20, 'fontname': 'Comic Sans MS', 'style': 'italic'})

    plt.savefig('skills_diagram.png', bbox_inches='tight')
    plt.show()
    plt.close()


create_diagram()
