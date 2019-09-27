TEMPLATE_FOLDER="SW01_Einfuehrung"
MAKEFILE="Makefile"
TEMPLATE_MAKEFILE="${TEMPLATE_FOLDER}/${MAKEFILE}"
METAFILE="00-meta.md"
TEMPLATE_METAFILE="${TEMPLATE_FOLDER}/${METAFILE}"

echo "Type the semesterweek?"
echo "  -> Format: [0-9][0-9]"
echo "  -> Example: 01"
read SEMESTERWEEK

echo "...and topic of the semesterweek ${SEMESTERWEEK}? "
echo "  -> Format: [a-zA-Z:CamelCase]"
echo "  -> Example: Einfuehrung_Modul"
read TOPIC
TOPIC_LOWERCASE=$(echo "${TOPIC}" | tr '[:upper:]' '[:lower:]')

FOLDERNAME="SW${SEMESTERWEEK}_${TOPIC}"

mkdir ${FOLDERNAME}
cp ${TEMPLATE_MAKEFILE} ${FOLDERNAME}/
cp ${TEMPLATE_METAFILE} ${FOLDERNAME}/

# Replace content of Makefile
sed -i "" "s/01_einfuehrung/${SEMESTERWEEK}_${TOPIC_LOWERCASE}/" ${FOLDERNAME}/${MAKEFILE}

# Replace content of 00-meta.md
sed -i "" "s/SW01/SW${SEMESTERWEEK}/" ${FOLDERNAME}/${METAFILE}