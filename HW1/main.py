import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./global_education_data.csv", encoding="cp437")


def main():
    # Q1:Top 5 countries with the highest out-of-school rate for primary age females
    top5_oosr_primary_females = df.nlargest(5, 'OOSR_Primary_Age_Female')[
        ['Countries and Areas', 'OOSR_Primary_Age_Female']]
    print("1.Top 5 countries with the highest out-of-school rate for primary age females\n", top5_oosr_primary_females,
          "\n\n")

    # Q2:Comparison of completion rate for upper secondary education between males and females
    upper_secondary_completion = df[['Completion_Rate_Upper_Secondary_Male', 'Completion_Rate_Upper_Secondary_Female']]
    for i in upper_secondary_completion.columns:
        plt.hist(df[i], density=True, alpha=0.3, label=i)  # overlapped hist to how the difference
    plt.legend()
    plt.savefig("./answer_pic/question2")
    plt.show()

    correlation = df["Youth_15_24_Literacy_Rate_Male"].corr(df['Unemployment_Rate'])
    print(f'Correlation between male youth literacy rate and unemployment rate: {correlation}')
    print("there is no obvious relation between male literacy rate and unemployment rate\n")
    sns.lmplot(data=df, x="Youth_15_24_Literacy_Rate_Male", y="Unemployment_Rate")
    plt.savefig("./answer_pic/question3")
    plt.show()

    # Q4: find out what OOSR rate and what Complete rate is most relevant
    oosr_columns = df.filter(like='OOSR_').columns.tolist()
    completion_columns = df.filter(like='Completion_Rate_').columns.tolist()
    correlation_matrix = pd.DataFrame(index=oosr_columns, columns=completion_columns)

    # Calculate the correlations and fill the matrix
    for oosr in oosr_columns:
        for completion in completion_columns:
            correlation_matrix.at[oosr, completion] = df[oosr].corr(df[completion])

    # print(correlation_matrix)
    abs_correlation_matrix = correlation_matrix.abs()

    # Find the maximum value and its position
    max_corr = abs_correlation_matrix.max().max()
    max_corr_position = abs_correlation_matrix.stack().idxmax()  # find it in stackoverflow

    print(
        f'Maximum absolute correlation: {max_corr} is the correlation between {max_corr_position[0]} and {max_corr_position[1]}')

    # Q5:Show the Countries and Areas
    plt.figure(figsize=(15, 10))
    plt.scatter(df['Longitude'], df['Latitude'], alpha=0.5)

    # Annotate each point with the country name
    for i, txt in enumerate(df['Countries and Areas']):
        plt.annotate(txt, (df['Longitude'][i], df['Latitude'][i]), textcoords="offset points", xytext=(0, 10),
                     ha='center')

    # Adjust the aesthetics
    plt.title('Countries and Areas by Latitude and Longitude')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)

    plt.savefig("./answer_pic/question5")
    plt.show()

    # Q6:Correlation between gross enrollment in tertiary education and unemployment rate
    correlation = df["Gross_Tertiary_Education_Enrollment"].corr(df['Unemployment_Rate'])
    print(f'Correlation between gross enrollment in tertiary education and unemployment rate: {correlation}')
    sns.lmplot(data=df, x="Gross_Tertiary_Education_Enrollment", y="Unemployment_Rate")
    plt.savefig("./answer_pic/question6")
    plt.show()


if __name__ == '__main__':
    main()
