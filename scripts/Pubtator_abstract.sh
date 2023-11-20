
# 软件下载
sh -c "$(curl -fsSL https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"
export PATH=${HOME}/edirect:${PATH}

# 获取PMID
esearch -db pubmed -mindate 2022/01/01 -maxdate 2022/10/31 -datetype PDAT -query "long covid" | efetch -format uid > idlist2.txt 

# 通过PubTator获取相关PMID的文献摘要
#!/bin/bash
F_OUT="result_MM_Pubtator.txt"
touch $F_OUT
F_LIST='idlist2.txt'
echo -e "\n I am curating the result of MM Jingbo\n"
echo -e '\n' >$F_OUT
i=1
while IFS= read -r line
do
curl https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/pubtator?pmids=$line >>$F_OUT
printf '$i -th result out of xxxxx is processing ...\n'
i=$[i+1]
sleep 5.8s
done <"$F_LIST"