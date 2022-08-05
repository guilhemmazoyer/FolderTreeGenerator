# Générateur d'arborescence de dossier

## Fonctionnemment
Le programme débute après que l'utilisateur ait choisit quel dossier traiter via le menu.
Le programme va ensuite lister les éléments contenus dans le dossier et vérifie si l'élément est un fichier ou un dossier. Si c'est un fichier, il note le nom du fichier dans le résultat et continue à lire les élémennts. Si c'est un dossier, il le note dans le résultat puis répète l'action précédente sur lui-même pour lire récursivement les informations des sous-dossiers.

## Réglages
Un premier réglage permet de définir la portée du programme, c'est à dire le nombre de niveau de sous-dossier auquel elle va accéder et afficher sur le résultat.<br>
Un second permet d'activer ou non la liste à ignorer par défaut.<br>
Le dernier permet d'activer ou non la liste à ignorer personnalisée.

### Listes à ignorer :
Il existe dans le programme 2 listes permettant d'ignorer dans dossier lors de l'exécution. Une liste par défaut, qui ignore les dossiers ".git", ".vscode" et "\_\_pycache\_\_". Et une liste personnalisée où chaque utilisateur peut renseigner ses mots clés à ignorer.

#### Exemples de liste personalisée :
_.git,.pycharm,assets_<br>
Cette liste, où les mots clés sont séparés par des virgules, ignore tous les dossiers se nommant .git ou .pycharm ou assets.

## Langues
Le programme est disponible en anglais et français. La langue peut être modifiée à la volée en passant par le menu textuel nommé "langue" ou en faisant Alt+F ou Alt+E.
Les traductions sont disposées dans un autre fichier auquel le GUI accède pour afficher les textes.

## Exemples
📁 assets<br>
&emsp;📁 documents<br>
&emsp;📁 fonts<br>
&emsp;&emsp;📄 ARSMaquettePro-Medium.ttf<br>
&emsp;&emsp;📄 ARSMaquettePro-Medium.zip<br>
&emsp;&emsp;📄 likesnow.ttf<br>
&emsp;&emsp;📄 Salsa-Regular.ttf<br>
&emsp;&emsp;📄 salsa.zip<br>
&emsp;&emsp;📄 Wall-Painter.ttf<br>
&emsp;&emsp;📄 wall-painter.zip<br>
&emsp;📁 images<br>
&emsp;&emsp;📄 capitaineCord.jpg<br>
&emsp;&emsp;📄 cdc.jpg<br>
&emsp;&emsp;📁 cv<br>
&emsp;&emsp;📄 desktop.ini<br>
&emsp;&emsp;📄 diagclasses.jpg<br>
&emsp;&emsp;📄 diagclasses.svg<br>
&emsp;&emsp;📄 difficulty.jpg<br>
&emsp;&emsp;📁 gamecards<br>
&emsp;&emsp;📄 gitlab.jpg<br>
&emsp;&emsp;📄 glanom_champs.jpg<br>
&emsp;&emsp;📄 glanom_foret.jpg<br>
&emsp;&emsp;📄 glanom_palais.jpg<br>
&emsp;&emsp;📄 glanom_rue.jpg<br>
&emsp;&emsp;📄 guilhem.jpg<br>
&emsp;&emsp;📄 home_background.jpg<br>
&emsp;&emsp;📁 icons<br>
&emsp;&emsp;📄 language.jpg<br>
&emsp;&emsp;📁 load<br>
&emsp;&emsp;📄 musiques_wt.jpg<br>
&emsp;&emsp;📄 polytech_pre.jpg<br>
&emsp;&emsp;📄 presentation_wt.jpg<br>
&emsp;&emsp;📁 reviews<br>
&emsp;&emsp;&emsp;📁 games-icon<br>
&emsp;&emsp;&emsp;📁 p-la<br>
&emsp;&emsp;&emsp;📁 sw-jfo<br>
&emsp;&emsp;&emsp;📁 tloz-botw<br>
&emsp;&emsp;...