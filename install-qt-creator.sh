#!/bin/sh -e

# SYNOPSIS
#
#     ./install-qt-creator.sh <major> <minor> <patch>
#     ./install-qt-creator.sh `python3 get_last_qt_creator_versions.py`
#
# COPYRIGHT
#
#     Dmitry Bravikov <dmitry@bravikov.pro>, 2019
#
# DESCRIPTION
#
#     The script downloads and updates or installs Qt Creator.
#
# EXAMPLE
#
#     Install Qt Creator 4.10.2:
#
#     ./install-qt-creator.sh 4 10 2

if [ $# -ne 3 ]
then
    echo "Bad arguments."
    echo "./update-qt-creator.sh <major> <minor> <patch>"
    exit 1
fi

DWLD_DEST_FOLDER="/mnt/data/Programs/Programing/QtCreator"

MAJOR=$1
MINOR=$2
PATCH=$3
SHORT_VERSION="$MAJOR.$MINOR"
FULL_VERSION="$SHORT_VERSION.$PATCH"
FILENAME="qt-creator-opensource-linux-x86_64-$FULL_VERSION.run"
URL="https://download.qt.io/official_releases/qtcreator/$SHORT_VERSION/$FULL_VERSION/$FILENAME"

[ ! -d "$DWLD_DEST_FOLDER" ] && DWLD_DEST_FOLDER=/tmp

INSTALLER="$DWLD_DEST_FOLDER/$FILENAME"

echo "$URL"
wget --show-progress -c "$URL" -O "$INSTALLER"
chmod u+x "$INSTALLER"
sudo "$INSTALLER"
