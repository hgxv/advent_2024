def is_safe(report, allow_removal=False):
    def is_valid_sequence(seq):
        # Vérifie si une séquence respecte les règles
        trend = None
        for i in range(len(seq) - 1):
            diff = seq[i] - seq[i + 1]
            if abs(diff) < 1 or abs(diff) > 3:
                return i  # Retourne l'indice de la première erreur
            current_trend = "increasing" if diff < 0 else "decreasing"
            if trend is None:
                trend = current_trend
            elif trend != current_trend:
                return i  # Retourne l'indice de la première erreur
        return None  # Aucun problème détecté

    # Vérifie si le rapport est valide sans suppression
    error_index = is_valid_sequence(report)
    if error_index is None:
        return True

    # Si une suppression est autorisée, teste jusqu'à trois suppressions possibles
    if allow_removal:
        candidates = []
        if error_index > 0:
            candidates.append(
                report[: error_index - 1] + report[error_index:]
            )  # Supprime avant l'erreur
        candidates.append(
            report[:error_index] + report[error_index + 1 :]
        )  # Supprime l'erreur
        if error_index + 1 < len(report):
            candidates.append(
                report[: error_index + 1] + report[error_index + 2 :]
            )  # Supprime après l'erreur

        # Vérifie si l'une des séquences candidates est valide
        return any(is_valid_sequence(candidate) is None for candidate in candidates)

    return False


# Lecture et analyse des données
safe_reports = 0

with open("input.txt", "r") as file:
    for line in file:
        levels = list(map(int, line.split()))
        if is_safe(levels, allow_removal=True):
            safe_reports += 1

print(safe_reports)
