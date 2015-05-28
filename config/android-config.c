#include <pwd.h>

int getpwuid_r(uid_t uid, struct passwd *pwd, char *buf, size_t buflen, struct passwd **result)
{
	*result = NULL;
	return 0;
}