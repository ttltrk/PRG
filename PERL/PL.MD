
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD)

###### [MUM](https://github.com/ttltrk/PRG/blob/master/MUM.MD) - [M](https://github.com/ttltrk/ELSE/blob/master/M/M.MD) || [PY](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD) - [UX](https://github.com/ttltrk/ELSE/blob/master/M/UX/UX.MD) || [ENG](https://github.com/ttltrk/ELSE/blob/master/LAN/ENG/LE.MD) - [DE](https://github.com/ttltrk/ELSE/blob/master/LAN/GER/DUO_GER.MD) - [SP](https://github.com/ttltrk/ELSE/blob/master/LAN/SP/SP.MD) || [Tools](https://github.com/ttltrk/ELSE/blob/master/M/TOOLS/TOOLS.MD)

---

<h3 id='^'>PERL</h3>

---

* <a href='#function'>function</a></br>
* <a href='#file'>file</a></br>
* <a href='#web'>web</a></br>

---

<h3 id='function'>function</h3>

```pl
sub elso {
	print "Hello, trk!\n";
	print "elso funkcio!\n";
}

elso

>>>
$ perl hw.pl
Hello, trk!
elso funkcio!
$
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='file'>file</h3>

```perl
use strict;
use warnings;

sub main {
    if (-f 'C:\Users\AttilaTorok\Desktop\ADM\MM\PL\WEB\logo.png') {
        print "Found file\n";
    }
    else {
        print "File not found\n";
    }
}

main();

>>>
Found file
>>>
```

```perl
use strict;
use warnings;

sub main {

    my $file = 'C:\Users\AttilaTorok\Desktop\ADM\MM\PL\WEB\logo.png';

    if (-f $file) {
        print "Found file\n";
    }
    else {
        print "File not found\n";
    }
}

main();

>>>
Found file
>>>
```

with Array

```perl
use strict;
use warnings;

sub main {

    #array
    my @files = (
        'C:\Users\AttilaTorok\Desktop\ADM\MM\PL\WEB\logo.png',
        'C:\Users\AttilaTorok\Desktop\ADM\MM\PL\WEB\home.html',
        'C:\Users\AttilaTorok\Desktop\ADM\MM\PL\WEB\home.txt',
    );

    foreach my $file(@files) { #how to iterate ower the array
        if ( -f $file ) {
            print "Found file: $file\n";
        }
        else {
            print "File not found: $file\n";
        }
    }
}

main();

>>>
Found file: C:\Users\AttilaTorok\Desktop\ADM\MM\PL\WEB\logo.png
Found file: C:\Users\AttilaTorok\Desktop\ADM\MM\PL\WEB\home.html
File not found: C:\Users\AttilaTorok\Desktop\ADM\MM\PL\WEB\home.txt
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='web'>web</h3>

get a webpage

```perl
use strict;
use warnings;
use LWP::Simple;

sub main {
    print "Downloading... \n";
    print get("http://www.google.com/");
    print "Finished!\n";
}

main();
```

store a webpage

```perl
use strict;
use warnings;
use LWP::Simple;

sub main {
    print "Downloading... \n";
    getstore("http://www.google.com/", "home.html");
    print "Finished!\n";
}

main();
```

```perl
use strict;
use warnings;
use LWP::Simple;

sub main {
    print "Downloading... \n";
    getstore('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', 'logo.png');
    print "Finished!\n";
}

main();
```

```perl
use strict;
use warnings;
use LWP::Simple;

sub main {
    print "Downloading... \n";
    my $code = getstore('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', 'logo.png');
    if($code == 200) {
        print "Success\n";
    }
    else {
        print "Failed\n";
    }
    print "Finished!\n";
}

main();
```

<a href='#^'>^^^</a>

---
