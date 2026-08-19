import pandas as pd 
import matplotlib.pyplot as plt 
from PIL import Image

#load the data:
df = pd.read_csv("netflix_titles.csv")
#print (df.head())

#clean data:
df = df.dropna(subset= ['type', 'release_year','rating', 'country', 'duration'])

fig, ax = plt.subplots(2, 4, figsize=(24, 10))

img=Image.open("Netflix_Logomark.png").convert("RGBA")
img=img.resize((500,500))
logo_ax=fig.add_axes([0.38,0.25,0.24,0.50],zorder=0)
logo_ax.imshow(img,alpha=0.03)
logo_ax.axis('off')
fig.patch.set_facecolor('#FFFFFF')

for a in ax.flat:
    a.set_facecolor('#FFFFFF')
    for spine in a.spines.values():
        spine.set_edgecolor('#E0E0E0')
    a.grid(axis='y',color='#F0F0F0',linewidth=0.7)
    a.tick_params(axis='both',labelsize=8)
    a.spines['top'].set_visible(False); a.spines['right'].set_visible(False)
    a.tick_params(axis='both',length=0)
    
type_counts = df['type'].value_counts()
ax[0,0].bar(type_counts.index,type_counts.values,color=['#E50914','#222222'])
ax[0,0].set_title("Number of Movies VS TV Shows on Netflix",fontweight='bold',fontsize=12,color='#222222')
ax[0,0].tick_params(axis='y',labelsize=9)
ax[0,0].set_xlabel("Type",fontsize=11,color='#555555')
ax[0,0].set_ylabel("Count",fontsize=10,color='#555555')


rating_counts = pd.concat([df["rating"].value_counts().head(5), pd.Series({"Other": df["rating"].value_counts().iloc[5:].sum()})])
wedges,text= ax[0,1].pie(rating_counts ,startangle = 90, wedgeprops=dict(width=0.4))
ax[0,1].text(0, 0,"CONTENT\nRATING",ha='center',va='center',fontweight='bold')
ax[0,1].legend(wedges,rating_counts.index,title="Rating",loc="upper center",bbox_to_anchor=(0.5,0.02),ncol=3,fontsize=9)
ax[0,1].set_title("Percentage of Content Rating",fontweight='bold',fontsize=12,color='#222222')

movie_df = df[df['type']=='Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace('min','').astype(int)
ax[0,2].hist(movie_df['duration_int'],bins=30,color='#E50914',edgecolor='#FFFFFF')
ax[0,2].set_title("Distribution of Movie Duration",fontweight='bold',fontsize=12,color='#222222')
ax[0,2].set_xlabel("Duration(minutes)",fontsize=10,color='#555555')
ax[0,2].set_ylabel("Number of Movies",fontsize=10,color='#555555')

director_counts=df['director'].dropna().str.split(', ').explode().value_counts().head(10)
ax[0,3].barh(director_counts.index[::-1],director_counts.values[::-1],color='#E50914')
ax[0,3].set_title("Top 10 Directors by Number of Titles",fontweight='bold',fontsize=12,color='#222222')
ax[0,3].bar_label(ax[0,3].containers[0],fontsize=8,padding=3)
ax[0,3].set_xlabel("Number of Titles")
ax[0,3].set_ylabel("Director")

country_counts = df['country'].value_counts().head(10)
ax[1,0].barh(country_counts.index,country_counts.values,color='#E50914')
ax[1,0].set_title("Top 10 countries by Number of Shows",fontweight='bold',fontsize=12,color='#222222')
ax[1,0].bar_label(ax[1,0].containers[0],fontsize=8,padding=3)
ax[1,0].set_xlabel("Number of Shows",fontsize=10,color='#555555')
ax[1,0].set_ylabel("Country",fontsize=10,color='#555555')

genre_counts = (df['listed_in'].str.split(', ').explode().value_counts().head(10))
ax[1,1].barh(genre_counts.index,genre_counts.values,color='#222222')
ax[1,1].set_title("Top 10 Genres on Netflix",fontweight='bold',fontsize=12,color='#222222')
ax[1,1].bar_label(ax[1,1].containers[0],fontsize=8,padding=3)
ax[1,1].set_xlabel("Number of Shows",fontsize=10,color='#555555')
ax[1,1].set_ylabel("Genre",fontsize=10,color='#555555')

content_by_year = df.pivot_table(index='release_year',columns='type',values='show_id',aggfunc='count')
ax[1,2].plot(content_by_year.index,content_by_year['Movie'],color='#E50914',linewidth=2)
ax[1,2].set_title("Movies Released Per Year",fontweight='bold',fontsize=12,color='#222222')
ax[1,2].set_xlabel("Year",fontsize=10,color='#555555')
ax[1,2].set_ylabel("Number of Movies",fontsize=10,color='#555555')

ax[1,3].plot(content_by_year.index,content_by_year['TV Show'],color='#222222',linewidth=2)
ax[1,3].set_title("TV Shows Released Per Year",fontweight='bold',fontsize=12,color='#222222')
ax[1,3].tick_params(axis='x',labelrotation=45,labelsize=8)
ax[1,3].set_xlabel("Year",fontsize=10,color='#555555')
ax[1,3].set_ylabel("Number of Shows",fontsize=10,color='#555555')


#fig.suptitle( "NETFLIX DATA ANALYSIS DASHBOARD",fontsize=28,fontweight='bold',color='red',bbox=dict(facecolor='black',edgecolor='red',boxstyle='round,pad=0.3' ))
fig.text(0.5, 0.96,"NETFLIX",ha='center',fontsize=30,fontweight='bold',fontname='DejaVu Sans',color='#E50914')
fig.text( 0.5, 0.925, "DATA ANALYSIS DASHBOARD", ha='center', fontsize=18, fontweight='bold',fontname='DejaVu Sans',color='#222222')
fig.lines.append(plt.Line2D([0.35,0.65],[0.90,0.90],transform=fig.transFigure,color='#E50914',linewidth=2))

plt.tight_layout(rect=[0.03,0,0.97,0.88])

plt.savefig('Netflix Data Analysis Dashboard .png', dpi =300 )
plt.show()