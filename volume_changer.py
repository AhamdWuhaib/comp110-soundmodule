"""
Module: volume_changer

Practice code for working with sounds in Python.
"""
import sound


def change_volume(original_sound):
    """
    Modifies the volume of the given sound.

    Parameters:
    original_sound (type: Sound): The original sound.

    Returns:
    Sound object: Like the original sound, but with the volume changed.
    """

    modified_sound = sound.copy(original_sound)
    multiplier = 2
    for sample_number in range(len(modified_sound)):
        sample = modified_sound[sample_number]

        # Change the left channel
        new_left_val = int(sample.left * multiplier)
        sample.left = new_left_val

        # Change the right channel
        new_right_val = int(sample.right * multiplier)
        sample.right = new_right_val

    return modified_sound

# First, test the change_volume with the love.wav audio
# love = sound.load_sound("love.wav")
# love.play()
# sound.wait_until_played()

# changed_love = change_volume(love)
# changed_love.play()
# sound.wait_until_played()


# Now, test our function with the doglake.wav audio
doglake_sound = sound.load_sound("doglake.wav")
doglake_sound.play()
sound.wait_until_played()

changed_doglake_sound = change_volume(doglake_sound)
changed_doglake_sound.play()
sound.wait_until_played()
