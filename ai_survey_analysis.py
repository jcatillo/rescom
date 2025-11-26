"""
Students' Perception, Trust, and Ethical Awareness of AI Tools in Education
Comprehensive Survey Analysis Report

This script analyzes survey responses regarding students' perspectives on AI in education,
including visualizations and theme extraction from open-ended questions.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
from wordcloud import WordCloud
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking plots
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Load the data
df = pd.read_csv('Research Question (Responses) - Form responses 1 (1).csv')

# Display basic information
print("="*80)
print("STUDENTS' PERCEPTION, TRUST, AND ETHICAL AWARENESS OF AI TOOLS IN EDUCATION")
print("="*80)
print(f"\nTotal Responses: {len(df)}")
print(f"Survey Period: {df['Timestamp'].min()} to {df['Timestamp'].max()}")
print("\n" + "="*80 + "\n")

# Clean column names for easier access
df.columns = df.columns.str.strip()

# ============================================================================
# SECTION 1: DEMOGRAPHIC ANALYSIS
# ============================================================================
print("\n" + "="*80)
print("SECTION 1: DEMOGRAPHIC OVERVIEW")
print("="*80 + "\n")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Demographic Overview of Survey Respondents', fontsize=16, fontweight='bold')

# 1.1 Degree Program Distribution
degree_counts = df['Degree Program'].value_counts()
print("Degree Program Distribution:")
print(degree_counts)
print()

ax1 = axes[0, 0]
colors = sns.color_palette("husl", len(degree_counts))
degree_counts.plot(kind='barh', ax=ax1, color=colors)
ax1.set_title('Distribution by Degree Program', fontsize=12, fontweight='bold')
ax1.set_xlabel('Number of Students')
ax1.set_ylabel('Degree Program')

# 1.2 Year Level Distribution
year_counts = df['Year Level'].value_counts().sort_index()
print("Year Level Distribution:")
print(year_counts)
print()

ax2 = axes[0, 1]
colors_year = sns.color_palette("coolwarm", len(year_counts))
year_counts.plot(kind='bar', ax=ax2, color=colors_year)
ax2.set_title('Distribution by Year Level', fontsize=12, fontweight='bold')
ax2.set_xlabel('Year Level')
ax2.set_ylabel('Number of Students')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=0)

# 1.3 All Degree Programs (Pie Chart)
ax3 = axes[1, 0]
# Show all programs without grouping into "Others"
ax3.pie(degree_counts, labels=degree_counts.index, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 8})
ax3.set_title('Degree Programs Distribution (Percentage)', fontsize=12, fontweight='bold')

# 1.4 Year Level Pie Chart
ax4 = axes[1, 1]
ax4.pie(year_counts, labels=year_counts.index, autopct='%1.1f%%', startangle=90, colors=colors_year)
ax4.set_title('Year Level Distribution (Percentage)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('01_demographics.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 01_demographics.png\n")

# ============================================================================
# SECTION 2: AI FAMILIARITY AND USAGE PATTERNS
# ============================================================================
print("\n" + "="*80)
print("SECTION 2: AI FAMILIARITY AND USAGE PATTERNS")
print("="*80 + "\n")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('AI Familiarity and Usage Patterns', fontsize=16, fontweight='bold')

# 2.1 Familiarity with AI
familiarity_col = 'How familiar are you with Artificial Intelligence (AI)?'
familiarity_order = ['Not familiar', 'Slightly familiar', 'Moderately familiar', 'Very familiar', 'Extremely familiar']
familiarity_counts = df[familiarity_col].value_counts()
print("AI Familiarity Levels:")
print(familiarity_counts)
print()

ax1 = axes[0, 0]
familiarity_counts.plot(kind='bar', ax=ax1, color=sns.color_palette("YlOrRd", len(familiarity_counts)))
ax1.set_title('How Familiar Are You with AI?', fontsize=12, fontweight='bold')
ax1.set_xlabel('Familiarity Level')
ax1.set_ylabel('Number of Students')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')

# 2.2 Frequency of AI Usage
usage_col = 'How often do you use AI tools for academic tasks?'
usage_order = ['Never', 'Rarely', 'Sometimes', 'Often', 'Daily']
usage_counts = df[usage_col].value_counts()
print("AI Usage Frequency:")
print(usage_counts)
print()

ax2 = axes[0, 1]
usage_counts.plot(kind='bar', ax=ax2, color=sns.color_palette("Blues_d", len(usage_counts)))
ax2.set_title('How Often Do You Use AI Tools?', fontsize=12, fontweight='bold')
ax2.set_xlabel('Frequency')
ax2.set_ylabel('Number of Students')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')

# 2.3 AI Tools Used
tools_col = 'Which AI tools have you used for schoolwork? (Check all that apply)'
all_tools = []
for tools in df[tools_col].dropna():
    if isinstance(tools, str):
        all_tools.extend([t.strip() for t in tools.split(',')])

tool_counts = Counter(all_tools)
print("AI Tools Used:")
for tool, count in tool_counts.most_common():
    print(f"  {tool}: {count}")
print()

ax3 = axes[1, 0]
tools_df = pd.Series(dict(tool_counts.most_common(10)))
tools_df.plot(kind='barh', ax=ax3, color=sns.color_palette("viridis", len(tools_df)))
ax3.set_title('Most Used AI Tools', fontsize=12, fontweight='bold')
ax3.set_xlabel('Number of Users')
ax3.set_ylabel('AI Tool')

# 2.4 Duration of AI Usage
duration_col = 'How long have you been using AI tools?'
duration_counts = df[duration_col].value_counts()
print("Duration of AI Usage:")
print(duration_counts)
print()

ax4 = axes[1, 1]
ax4.pie(duration_counts, labels=duration_counts.index, autopct='%1.1f%%', startangle=90)
ax4.set_title('How Long Have You Been Using AI?', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('02_familiarity_usage.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 02_familiarity_usage.png\n")

# ============================================================================
# SECTION 3: PERCEPTION OF AI IN LEARNING
# ============================================================================
print("\n" + "="*80)
print("SECTION 3: PERCEPTION OF AI IN LEARNING")
print("="*80 + "\n")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Student Perceptions of AI in Learning', fontsize=16, fontweight='bold')

# 3.1 AI Improves Learning
learning_col = 'Do you believe AI improves the learning process?'
learning_counts = df[learning_col].value_counts()
print("Does AI Improve Learning?")
print(learning_counts)
print()

ax1 = axes[0, 0]
learning_counts.plot(kind='bar', ax=ax1, color=sns.color_palette("Greens_d", len(learning_counts)))
ax1.set_title('Does AI Improve the Learning Process?', fontsize=12, fontweight='bold')
ax1.set_xlabel('Response')
ax1.set_ylabel('Number of Students')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')

# 3.2 Helpfulness of AI
helpful_col = 'How helpful do you find AI when doing assignments or projects?'
helpful_counts = df[helpful_col].value_counts()
print("AI Helpfulness:")
print(helpful_counts)
print()

ax2 = axes[0, 1]
helpful_counts.plot(kind='bar', ax=ax2, color=sns.color_palette("RdYlGn", len(helpful_counts)))
ax2.set_title('How Helpful is AI for Assignments?', fontsize=12, fontweight='bold')
ax2.set_xlabel('Helpfulness Level')
ax2.set_ylabel('Number of Students')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')

# 3.3 Interest in Learning More
interest_col = 'How interested are you in learning more about Artificial Intelligence?'
interest_counts = df[interest_col].value_counts()
print("Interest in Learning More:")
print(interest_counts)
print()

ax3 = axes[1, 0]
ax3.pie(interest_counts, labels=interest_counts.index, autopct='%1.1f%%', startangle=90)
ax3.set_title('Interest in Learning More About AI', fontsize=12, fontweight='bold')

# 3.4 Would Take AI Course
course_col = 'Would you take an AI-related course if your school offered one?'
course_counts = df[course_col].value_counts()
print("Would Take AI Course:")
print(course_counts)
print()

ax4 = axes[1, 1]
colors_course = ['#2ecc71', '#f39c12', '#e74c3c']
course_counts.plot(kind='bar', ax=ax4, color=colors_course[:len(course_counts)])
ax4.set_title('Would You Take an AI Course?', fontsize=12, fontweight='bold')
ax4.set_xlabel('Response')
ax4.set_ylabel('Number of Students')
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=0)

plt.tight_layout()
plt.savefig('03_learning_perception.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 03_learning_perception.png\n")

# ============================================================================
# SECTION 4: TRUST AND ACCURACY PERCEPTIONS
# ============================================================================
print("\n" + "="*80)
print("SECTION 4: TRUST AND ACCURACY PERCEPTIONS")
print("="*80 + "\n")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Trust and Accuracy Perceptions', fontsize=16, fontweight='bold')

# 4.1 Perceived Accuracy
accuracy_col = 'How accurate do you think AI-generated content usually is?'
accuracy_counts = df[accuracy_col].value_counts()
print("Perceived Accuracy of AI Content:")
print(accuracy_counts)
print()

ax1 = axes[0, 0]
accuracy_counts.plot(kind='bar', ax=ax1, color=sns.color_palette("Oranges_d", len(accuracy_counts)))
ax1.set_title('Perceived Accuracy of AI-Generated Content', fontsize=12, fontweight='bold')
ax1.set_xlabel('Accuracy Level')
ax1.set_ylabel('Number of Students')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')

# 4.2 Frequency of Double-Checking
doublecheck_col = 'How often do you double-check information produced by AI tools?'
doublecheck_counts = df[doublecheck_col].value_counts()
print("Frequency of Double-Checking AI Output:")
print(doublecheck_counts)
print()

ax2 = axes[0, 1]
doublecheck_counts.plot(kind='bar', ax=ax2, color=sns.color_palette("Purples_d", len(doublecheck_counts)))
ax2.set_title('How Often Do You Double-Check AI Information?', fontsize=12, fontweight='bold')
ax2.set_xlabel('Frequency')
ax2.set_ylabel('Number of Students')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')

# 4.3 Concern About Incorrect Information
concern_col = 'Are you concerned about AI producing incorrect or misleading information?'
concern_counts = df[concern_col].value_counts()
print("Concern About Incorrect Information:")
print(concern_counts)
print()

ax3 = axes[1, 0]
colors_concern = ['#e74c3c', '#f39c12', '#95a5a6']
concern_counts.plot(kind='bar', ax=ax3, color=colors_concern[:len(concern_counts)])
ax3.set_title('Concerned About Incorrect/Misleading Information?', fontsize=12, fontweight='bold')
ax3.set_xlabel('Response')
ax3.set_ylabel('Number of Students')
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=0)

# 4.4 Worry About Plagiarism
plagiarism_col = 'Do you worry about plagiarism when using AI tools?'
plagiarism_counts = df[plagiarism_col].value_counts()
print("Worry About Plagiarism:")
print(plagiarism_counts)
print()

ax4 = axes[1, 1]
plagiarism_counts.plot(kind='bar', ax=ax4, color=colors_concern[:len(plagiarism_counts)])
ax4.set_title('Do You Worry About Plagiarism?', fontsize=12, fontweight='bold')
ax4.set_xlabel('Response')
ax4.set_ylabel('Number of Students')
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=0)

plt.tight_layout()
plt.savefig('04_trust_accuracy.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 04_trust_accuracy.png\n")

# ============================================================================
# SECTION 5: ETHICAL AWARENESS AND FUTURE OUTLOOK
# ============================================================================
print("\n" + "="*80)
print("SECTION 5: ETHICAL AWARENESS AND FUTURE OUTLOOK")
print("="*80 + "\n")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Ethical Awareness and Future Outlook', fontsize=16, fontweight='bold')

# 5.1 Need for Clear Guidelines
guidelines_col = 'Do you think schools should have clear guidelines for AI usage?'
guidelines_counts = df[guidelines_col].value_counts()
print("Should Schools Have Clear AI Guidelines?")
print(guidelines_counts)
print()

ax1 = axes[0, 0]
colors_yes = ['#2ecc71', '#f39c12', '#e74c3c']
guidelines_counts.plot(kind='bar', ax=ax1, color=colors_yes[:len(guidelines_counts)])
ax1.set_title('Should Schools Have Clear AI Guidelines?', fontsize=12, fontweight='bold')
ax1.set_xlabel('Response')
ax1.set_ylabel('Number of Students')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=0)

# 5.2 AI Skills Important for Future Careers
career_col = 'Do you think AI and automation skills will be important in future careers?'
career_counts = df[career_col].value_counts()
print("AI Skills Important for Future Careers?")
print(career_counts)
print()

ax2 = axes[0, 1]
career_counts.plot(kind='bar', ax=ax2, color=sns.color_palette("Blues_d", len(career_counts)))
ax2.set_title('Are AI Skills Important for Future Careers?', fontsize=12, fontweight='bold')
ax2.set_xlabel('Response')
ax2.set_ylabel('Number of Students')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')

# 5.3 Participate in AI Research
research_col = 'Would you participate in AI-related research or school projects?'
research_counts = df[research_col].value_counts()
print("Would Participate in AI Research:")
print(research_counts)
print()

ax3 = axes[1, 0]
ax3.pie(research_counts, labels=research_counts.index, autopct='%1.1f%%', startangle=90)
ax3.set_title('Would You Participate in AI Research?', fontsize=12, fontweight='bold')

# 5.4 Summary Statistics
ax4 = axes[1, 1]
ax4.axis('off')
summary_text = f"""
KEY FINDINGS - ETHICAL AWARENESS

• {guidelines_counts.get('Yes', 0)} students ({guidelines_counts.get('Yes', 0)/len(df)*100:.1f}%) believe 
  schools should have clear AI guidelines

• {career_counts.get('Strongly agree', 0) + career_counts.get('Agree', 0)} students 
  ({(career_counts.get('Strongly agree', 0) + career_counts.get('Agree', 0))/len(df)*100:.1f}%) 
  agree AI skills are important for careers

• {concern_counts.get('Yes', 0)} students ({concern_counts.get('Yes', 0)/len(df)*100:.1f}%) are 
  concerned about incorrect information

• {plagiarism_counts.get('Yes', 0)} students ({plagiarism_counts.get('Yes', 0)/len(df)*100:.1f}%) 
  worry about plagiarism
"""
ax4.text(0.1, 0.5, summary_text, fontsize=11, verticalalignment='center', 
         family='monospace', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('05_ethical_awareness.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 05_ethical_awareness.png\n")

# ============================================================================
# SECTION 6: THEME EXTRACTION FROM OPEN-ENDED QUESTIONS
# ============================================================================
print("\n" + "="*80)
print("SECTION 6: THEME EXTRACTION FROM OPEN-ENDED QUESTIONS")
print("="*80 + "\n")

def extract_keywords(text_series, min_word_length=4, top_n=20):
    """Extract common keywords from text responses"""
    if text_series is None:
        return Counter()
    
    # Common stop words to exclude
    stop_words = {'that', 'this', 'with', 'from', 'have', 'more', 'about', 'would', 
                  'their', 'there', 'when', 'where', 'which', 'while', 'also', 'make',
                  'like', 'just', 'some', 'such', 'into', 'them', 'than', 'then',
                  'these', 'those', 'very', 'what', 'been', 'were', 'they', 'your',
                  'should', 'could', 'will', 'can', 'may', 'might', 'must', 'shall'}
    
    all_words = []
    for text in text_series.dropna():
        if isinstance(text, str) and text.strip() and text.lower() not in ['na', 'n/a', 'none', 'nothing']:
            # Clean and tokenize
            words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
            # Filter words
            words = [w for w in words if len(w) >= min_word_length and w not in stop_words]
            all_words.extend(words)
    
    return Counter(all_words)

# 6.1 Learning Experience Influences
print("Analyzing: How AI has influenced learning experience...")
learning_exp_col = 'In what ways has AI influenced your learning experience?'
learning_keywords = extract_keywords(df[learning_exp_col], top_n=15)

print("\nTop themes in 'Learning Experience':")
for word, count in learning_keywords.most_common(15):
    print(f"  {word}: {count}")

# 6.2 Trustworthiness Factors
print("\nAnalyzing: Factors that determine trustworthiness...")
trust_col = 'What factors help you decide if an AI-generated answer is trustworthy?'
trust_keywords = extract_keywords(df[trust_col], top_n=15)

print("\nTop themes in 'Trustworthiness Factors':")
for word, count in trust_keywords.most_common(15):
    print(f"  {word}: {count}")

# 6.3 Ethical Concerns
print("\nAnalyzing: Ethical concerns about AI in education...")
ethics_col = 'What ethical concerns do you have about using AI in education?'
ethics_keywords = extract_keywords(df[ethics_col], top_n=15)

print("\nTop themes in 'Ethical Concerns':")
for word, count in ethics_keywords.most_common(15):
    print(f"  {word}: {count}")

# 6.4 Skills to Learn
print("\nAnalyzing: AI skills students want to learn...")
skills_col = 'What AI skills or topics would you like to learn more about?'
skills_keywords = extract_keywords(df[skills_col], top_n=15)

print("\nTop themes in 'Skills to Learn':")
for word, count in skills_keywords.most_common(15):
    print(f"  {word}: {count}")

# 6.5 Suggested Improvements
print("\nAnalyzing: Suggested improvements for AI tools...")
improvements_col = 'What improvements would you suggest for AI tools used in education?'
improvements_keywords = extract_keywords(df[improvements_col], top_n=15)

print("\nTop themes in 'Suggested Improvements':")
for word, count in improvements_keywords.most_common(15):
    print(f"  {word}: {count}")

# Visualize themes
fig, axes = plt.subplots(3, 2, figsize=(18, 16))
fig.suptitle('Recurring Themes in Open-Ended Responses', fontsize=16, fontweight='bold')

# Theme 1: Learning Experience
ax1 = axes[0, 0]
learning_df = pd.Series(dict(learning_keywords.most_common(12)))
learning_df.plot(kind='barh', ax=ax1, color=sns.color_palette("viridis", len(learning_df)))
ax1.set_title('Learning Experience Themes', fontsize=12, fontweight='bold')
ax1.set_xlabel('Frequency')

# Theme 2: Trustworthiness
ax2 = axes[0, 1]
trust_df = pd.Series(dict(trust_keywords.most_common(12)))
trust_df.plot(kind='barh', ax=ax2, color=sns.color_palette("plasma", len(trust_df)))
ax2.set_title('Trustworthiness Factor Themes', fontsize=12, fontweight='bold')
ax2.set_xlabel('Frequency')

# Theme 3: Ethical Concerns
ax3 = axes[1, 0]
ethics_df = pd.Series(dict(ethics_keywords.most_common(12)))
ethics_df.plot(kind='barh', ax=ax3, color=sns.color_palette("magma", len(ethics_df)))
ax3.set_title('Ethical Concern Themes', fontsize=12, fontweight='bold')
ax3.set_xlabel('Frequency')

# Theme 4: Skills to Learn
ax4 = axes[1, 1]
skills_df = pd.Series(dict(skills_keywords.most_common(12)))
skills_df.plot(kind='barh', ax=ax4, color=sns.color_palette("cividis", len(skills_df)))
ax4.set_title('Desired AI Skills/Topics', fontsize=12, fontweight='bold')
ax4.set_xlabel('Frequency')

# Theme 5: Improvements
ax5 = axes[2, 0]
improvements_df = pd.Series(dict(improvements_keywords.most_common(12)))
improvements_df.plot(kind='barh', ax=ax5, color=sns.color_palette("coolwarm", len(improvements_df)))
ax5.set_title('Suggested Improvement Themes', fontsize=12, fontweight='bold')
ax5.set_xlabel('Frequency')

# Theme 6: Combined Word Cloud
ax6 = axes[2, 1]
all_open_ended = pd.concat([
    df[learning_exp_col],
    df[trust_col],
    df[ethics_col],
    df[skills_col],
    df[improvements_col]
])
all_text = ' '.join([str(t) for t in all_open_ended.dropna() if str(t).lower() not in ['na', 'n/a', 'none']])
if all_text:
    wordcloud = WordCloud(width=800, height=400, background_color='white', 
                          colormap='viridis', max_words=50).generate(all_text)
    ax6.imshow(wordcloud, interpolation='bilinear')
    ax6.axis('off')
    ax6.set_title('Word Cloud - All Open-Ended Responses', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('06_theme_extraction.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: 06_theme_extraction.png\n")

# ============================================================================
# SECTION 7: RELATIONSHIP ANALYSIS
# ============================================================================
print("\n" + "="*80)
print("SECTION 7: RELATIONSHIP ANALYSIS")
print("="*80 + "\n")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Relationships Between Variables', fontsize=16, fontweight='bold')

# 7.1 Familiarity vs Usage Frequency
ax1 = axes[0, 0]
familiarity_usage = pd.crosstab(df[familiarity_col], df[usage_col])
familiarity_usage.plot(kind='bar', stacked=True, ax=ax1, colormap='viridis')
ax1.set_title('AI Familiarity vs Usage Frequency', fontsize=12, fontweight='bold')
ax1.set_xlabel('Familiarity Level')
ax1.set_ylabel('Count')
ax1.legend(title='Usage Frequency', bbox_to_anchor=(1.05, 1), loc='upper left')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')

# 7.2 Year Level vs AI Familiarity
ax2 = axes[0, 1]
year_familiarity = pd.crosstab(df['Year Level'], df[familiarity_col])
year_familiarity.plot(kind='bar', stacked=True, ax=ax2, colormap='plasma')
ax2.set_title('Year Level vs AI Familiarity', fontsize=12, fontweight='bold')
ax2.set_xlabel('Year Level')
ax2.set_ylabel('Count')
ax2.legend(title='Familiarity', bbox_to_anchor=(1.05, 1), loc='upper left')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=0)

# 7.3 Helpfulness vs Concern about Accuracy
ax3 = axes[1, 0]
helpful_concern = pd.crosstab(df[helpful_col], df[concern_col])
helpful_concern.plot(kind='bar', stacked=True, ax=ax3, color=['#e74c3c', '#f39c12', '#95a5a6'])
ax3.set_title('AI Helpfulness vs Concern About Incorrect Info', fontsize=12, fontweight='bold')
ax3.set_xlabel('Helpfulness Level')
ax3.set_ylabel('Count')
ax3.legend(title='Concerned?', bbox_to_anchor=(1.05, 1), loc='upper left')
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45, ha='right')

# 7.4 Familiarity vs Interest in Learning More
ax4 = axes[1, 1]
familiarity_interest = pd.crosstab(df[familiarity_col], df[interest_col])
familiarity_interest.plot(kind='bar', stacked=True, ax=ax4, colormap='RdYlGn')
ax4.set_title('AI Familiarity vs Interest in Learning More', fontsize=12, fontweight='bold')
ax4.set_xlabel('Familiarity Level')
ax4.set_ylabel('Count')
ax4.legend(title='Interest Level', bbox_to_anchor=(1.05, 1), loc='upper left')
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.savefig('07_relationships.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 07_relationships.png\n")

# ============================================================================
# SECTION 8: CORRELATION HEATMAP
# ============================================================================
print("\n" + "="*80)
print("SECTION 8: CORRELATION ANALYSIS")
print("="*80 + "\n")

# Create numeric mappings for ordinal variables
familiarity_map = {'Not familiar': 1, 'Slightly familiar': 2, 'Moderately familiar': 3, 
                   'Very familiar': 4, 'Extremely familiar': 5}
usage_map = {'Never': 1, 'Rarely': 2, 'Sometimes': 3, 'Often': 4, 'Daily': 5}
helpful_map = {'Not helpful': 1, 'Slightly helpful': 2, 'Moderately helpful': 3, 
               'Very helpful': 4, 'Extremely helpful': 5}
accuracy_map = {'Not accurate': 1, 'Slightly accurate': 2, 'Moderately accurate': 3, 
                'Very accurate': 4, 'Extremely accurate': 5}
interest_map = {'Not interested': 1, 'Slightly Interested': 2, 'Moderately interested': 3, 
                'Very interested': 4, 'Extremely interested': 5}
agreement_map = {'Strongly disagree': 1, 'Disagree': 2, 'Neutral': 3, 'Agree': 4, 'Strongly Agree': 5}

# Create numeric dataframe
numeric_df = pd.DataFrame({
    'Familiarity': df[familiarity_col].map(familiarity_map),
    'Usage_Frequency': df[usage_col].map(usage_map),
    'Helpfulness': df[helpful_col].map(helpful_map),
    'Perceived_Accuracy': df[accuracy_col].map(accuracy_map),
    'Interest_in_AI': df[interest_col].map(interest_map),
    'Improves_Learning': df[learning_col].map(agreement_map),
    'AI_Career_Important': df[career_col].map(agreement_map)
})

# Calculate correlation
correlation_matrix = numeric_df.corr()

fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
            square=True, linewidths=1, cbar_kws={"shrink": 0.8}, ax=ax)
ax.set_title('Correlation Matrix - Key Variables', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('08_correlation_matrix.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 08_correlation_matrix.png\n")

print("\nKey Correlations:")
# Get top correlations (excluding diagonal)
corr_pairs = []
for i in range(len(correlation_matrix.columns)):
    for j in range(i+1, len(correlation_matrix.columns)):
        corr_pairs.append((
            correlation_matrix.columns[i],
            correlation_matrix.columns[j],
            correlation_matrix.iloc[i, j]
        ))
corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)

for var1, var2, corr in corr_pairs[:10]:
    print(f"  {var1} ↔ {var2}: {corr:.3f}")

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n" + "="*80)
print("ANALYSIS COMPLETE - SUMMARY")
print("="*80 + "\n")

print("Generated Visualizations:")
print("  1. 01_demographics.png - Demographic overview")
print("  2. 02_familiarity_usage.png - AI familiarity and usage patterns")
print("  3. 03_learning_perception.png - Perception of AI in learning")
print("  4. 04_trust_accuracy.png - Trust and accuracy perceptions")
print("  5. 05_ethical_awareness.png - Ethical awareness and future outlook")
print("  6. 06_theme_extraction.png - Recurring themes from open-ended questions")
print("  7. 07_relationships.png - Relationships between variables")
print("  8. 08_correlation_matrix.png - Correlation analysis")

print("\n" + "="*80)
print("KEY INSIGHTS")
print("="*80 + "\n")

print(f"1. ADOPTION & FAMILIARITY:")
print(f"   • {(df[familiarity_col].isin(['Very familiar', 'Extremely familiar']).sum() / len(df) * 100):.1f}% are very/extremely familiar with AI")
print(f"   • {(df[usage_col].isin(['Often', 'Daily']).sum() / len(df) * 100):.1f}% use AI tools often or daily")
print(f"   • Most popular tool: {tool_counts.most_common(1)[0][0]} ({tool_counts.most_common(1)[0][1]} users)")

print(f"\n2. PERCEPTION & VALUE:")
print(f"   • {(df[learning_col].isin(['Agree', 'Strongly Agree']).sum() / len(df) * 100):.1f}% agree AI improves learning")
print(f"   • {(df[helpful_col].isin(['Very helpful', 'Extremely helpful']).sum() / len(df) * 100):.1f}% find AI very/extremely helpful")

print(f"\n3. TRUST & VERIFICATION:")
print(f"   • {(df[doublecheck_col].isin(['Always', 'Often']).sum() / len(df) * 100):.1f}% always/often double-check AI output")
print(f"   • {(df[concern_col] == 'Yes').sum() / len(df) * 100:.1f}% concerned about incorrect information")
print(f"   • Top trustworthiness factors: {', '.join([w for w, c in trust_keywords.most_common(3)])}")

print(f"\n4. ETHICAL AWARENESS:")
print(f"   • {(df[plagiarism_col] == 'Yes').sum() / len(df) * 100:.1f}% worry about plagiarism")
print(f"   • {(df[guidelines_col] == 'Yes').sum() / len(df) * 100:.1f}% want clear school guidelines")
print(f"   • Top ethical concerns: {', '.join([w for w, c in ethics_keywords.most_common(3)])}")

print(f"\n5. FUTURE OUTLOOK:")
print(f"   • {(df[career_col].isin(['Agree', 'Strongly agree']).sum() / len(df) * 100):.1f}% believe AI skills are important for careers")
course_yes_pct = (df[course_col] == 'Yes').sum() / len(df) * 100
print(f"   • {course_yes_pct:.1f}% would take an AI course")
print(f"   • Top skills to learn: {', '.join([w for w, c in skills_keywords.most_common(3)])}")

print("\n" + "="*80)
print("Report generation complete!")
print("="*80)

# ============================================================================
# GENERATE PDF REPORT
# ============================================================================
print("\n" + "="*80)
print("GENERATING PDF REPORT")
print("="*80 + "\n")

try:
    import subprocess
    import os
    
    # Check if markdown file exists
    if os.path.exists('AI_Survey_Report.md'):
        print("Converting AI_Survey_Report.md to PDF...")
        
        # Try using pandoc (most reliable)
        try:
            result = subprocess.run(
                ['pandoc', 'AI_Survey_Report.md', '-o', 'AI_Survey_Report.pdf', 
                 '--pdf-engine=xelatex', '-V', 'geometry:margin=1in'],
                capture_output=True,
                text=True,
                timeout=60
            )
            if result.returncode == 0:
                print("✓ Successfully generated: AI_Survey_Report.pdf (using pandoc)")
            else:
                raise Exception("Pandoc failed")
        except (FileNotFoundError, Exception):
            # Fallback: Try using markdown-pdf via npm
            try:
                result = subprocess.run(
                    ['markdown-pdf', 'AI_Survey_Report.md'],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                if result.returncode == 0:
                    print("✓ Successfully generated: AI_Survey_Report.pdf (using markdown-pdf)")
                else:
                    raise Exception("markdown-pdf failed")
            except (FileNotFoundError, Exception):
                # Final fallback: Use Python's markdown + weasyprint
                try:
                    import markdown
                    from weasyprint import HTML, CSS
                    
                    # Read markdown file
                    with open('AI_Survey_Report.md', 'r', encoding='utf-8') as f:
                        md_content = f.read()
                    
                    # Convert markdown to HTML
                    html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
                    
                    # Add CSS styling
                    styled_html = f"""
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <meta charset="utf-8">
                        <style>
                            body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
                            h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
                            h2 {{ color: #34495e; margin-top: 30px; border-bottom: 2px solid #95a5a6; padding-bottom: 5px; }}
                            h3 {{ color: #7f8c8d; }}
                            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
                            th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
                            th {{ background-color: #3498db; color: white; }}
                            code {{ background-color: #f4f4f4; padding: 2px 6px; border-radius: 3px; }}
                            blockquote {{ border-left: 4px solid #3498db; padding-left: 20px; margin: 20px 0; background-color: #ecf0f1; }}
                        </style>
                    </head>
                    <body>
                        {html_content}
                    </body>
                    </html>
                    """
                    
                    # Generate PDF
                    HTML(string=styled_html).write_pdf('AI_Survey_Report.pdf')
                    print("✓ Successfully generated: AI_Survey_Report.pdf (using weasyprint)")
                    
                except ImportError:
                    print("⚠ PDF generation skipped: No PDF converter available")
                    print("  Install one of the following:")
                    print("    - pandoc: brew install pandoc (recommended)")
                    print("    - markdown-pdf: npm install -g markdown-pdf")
                    print("    - weasyprint: pip3 install markdown weasyprint")
    else:
        print("⚠ AI_Survey_Report.md not found, skipping PDF generation")
        
except Exception as e:
    print(f"⚠ PDF generation failed: {e}")
    print("  The markdown report is still available: AI_Survey_Report.md")

print("\n" + "="*80)
print("ALL OUTPUTS GENERATED")
print("="*80)
print("\nFiles created:")
print("  • 8 PNG visualizations (01-08)")
print("  • AI_Survey_Report.md (markdown report)")
if os.path.exists('AI_Survey_Report.pdf'):
    print("  • AI_Survey_Report.pdf (PDF report)")
print("\n" + "="*80)
