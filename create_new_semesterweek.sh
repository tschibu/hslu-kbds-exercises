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
# sed -i "" "s/01_einfuehrung/${SEMESTERWEEK}_${TOPIC_LOWERCASE}/" ${FOLDERNAME}/${MAKEFILE}
python -c "
import sys

param_replace = str(sys.argv[1])
param_file = str(sys.argv[2])

# Read in the file
with open(param_file, 'r') as file :
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('01_einfuehrung', param_replace)

# Write the file out again
with open(param_file, 'w') as file :
    file.write(filedata)
" ${SEMESTERWEEK}_${TOPIC_LOWERCASE} ${FOLDERNAME}/${MAKEFILE}

# Replace content of 00-meta.md
# sed -i "" "s/SW01/SW${SEMESTERWEEK}/" ${FOLDERNAME}/${METAFILE}
python -c "
import sys

param_replace = str(sys.argv[1])
param_file = str(sys.argv[2])

# Read in the file
with open(param_file, 'r') as file :
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('SW01', param_replace)

# Write the file out again
with open(param_file, 'w') as file :
    file.write(filedata)
" SW${SEMESTERWEEK} ${FOLDERNAME}/${METAFILE}

echo "# Testatübung SW${SEMESTERWEEK}" > ${FOLDERNAME}/01-testatuebungen.md